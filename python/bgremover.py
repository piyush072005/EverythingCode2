import io
import threading
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

from PIL import Image, ImageTk


class BackgroundRemoverApp(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Background Remover")
		self.geometry("1000x650")
		self.minsize(900, 600)

		# State
		self.original_image: Image.Image | None = None
		self.processed_image: Image.Image | None = None
		self.original_path: Path | None = None

		# Keep references to PhotoImage to avoid GC
		self._original_photo = None
		self._processed_photo = None

		# UI
		self._build_ui()

	def _build_ui(self):
		# Top controls
		control_frame = ttk.Frame(self, padding=(10, 10))
		control_frame.pack(side=tk.TOP, fill=tk.X)

		self.open_btn = ttk.Button(control_frame, text="Open Image", command=self.open_image)
		self.open_btn.pack(side=tk.LEFT, padx=(0, 8))

		self.remove_btn = ttk.Button(control_frame, text="Remove Background", command=self.remove_background)
		self.remove_btn.pack(side=tk.LEFT, padx=(0, 8))
		self.remove_btn.state(["disabled"])  # disabled until an image is loaded

		self.save_btn = ttk.Button(control_frame, text="Save Result", command=self.save_result)
		self.save_btn.pack(side=tk.LEFT, padx=(0, 8))
		self.save_btn.state(["disabled"])  # disabled until processed

		self.clear_btn = ttk.Button(control_frame, text="Clear", command=self.clear_images)
		self.clear_btn.pack(side=tk.LEFT, padx=(0, 8))

		# Progress bar
		self.progress = ttk.Progressbar(control_frame, mode="indeterminate", length=200)
		self.progress.pack(side=tk.LEFT, padx=(16, 0))

		# Preview area
		preview_frame = ttk.Frame(self, padding=10)
		preview_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		left_frame = ttk.LabelFrame(preview_frame, text="Original", padding=8)
		left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 6))
		right_frame = ttk.LabelFrame(preview_frame, text="Result", padding=8)
		right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(6, 0))

		self.original_label = ttk.Label(left_frame, anchor=tk.CENTER)
		self.original_label.pack(fill=tk.BOTH, expand=True)

		self.processed_label = ttk.Label(right_frame, anchor=tk.CENTER)
		self.processed_label.pack(fill=tk.BOTH, expand=True)

		# Footer hint
		hint = ttk.Label(
			self,
			padding=(10, 0),
			text="Tip: Use high-contrast images for best results. Output is PNG with transparency.",
		)
		hint.pack(side=tk.BOTTOM, anchor=tk.W)

	# -------- Helpers --------
	def _enable(self, widget: ttk.Button, enable: bool):
		if enable:
			widget.state(["!disabled"])  # remove disabled
		else:
			widget.state(["disabled"])  # add disabled

	def _fit_for_label(self, img: Image.Image, label: ttk.Label) -> Image.Image:
		# Compute target size from current label size
		label.update_idletasks()
		w = max(label.winfo_width(), 300)
		h = max(label.winfo_height(), 300)
		img_w, img_h = img.size
		scale = min(w / img_w, h / img_h)
		new_size = (max(1, int(img_w * scale)), max(1, int(img_h * scale)))
		return img.resize(new_size, Image.LANCZOS)

	def _render_to_label(self, img: Image.Image, label: ttk.Label, is_result=False):
		fitted = self._fit_for_label(img, label)
		photo = ImageTk.PhotoImage(fitted)
		label.configure(image=photo)
		label.image = photo  # tie lifecycle to label
		if is_result:
			self._processed_photo = photo
		else:
			self._original_photo = photo

	# -------- Actions --------
	def open_image(self):
		file_path = filedialog.askopenfilename(
			title="Select an image",
			filetypes=[
				("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
				("PNG", "*.png"),
				("JPEG", "*.jpg;*.jpeg"),
				("All files", "*.*"),
			],
		)
		if not file_path:
			return

		try:
			img = Image.open(file_path).convert("RGBA")
		except Exception as e:
			messagebox.showerror("Error", f"Could not open image:\n{e}")
			return

		self.original_image = img
		self.processed_image = None
		self.original_path = Path(file_path)

		self._render_to_label(self.original_image, self.original_label)
		self.processed_label.configure(image="")
		self.processed_label.image = None

		self._enable(self.remove_btn, True)
		self._enable(self.save_btn, False)

	def remove_background(self):
		if self.original_image is None:
			messagebox.showinfo("No image", "Please open an image first.")
			return

		# Try importing rembg lazily to allow GUI to open without it
		try:
			from rembg import remove  # type: ignore
		except Exception:
			messagebox.showerror(
				"Dependency missing",
				"The 'rembg' package is not installed. Please install it via requirements.txt.",
			)
			return

		def work():
			try:
				# Convert input image to bytes
				buf = io.BytesIO()
				self.original_image.save(buf, format="PNG")
				input_bytes = buf.getvalue()

				# Run removal
				output_bytes = remove(input_bytes)
				out_img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

				self.processed_image = out_img
				# Update UI on main thread
				self.after(0, lambda: self._render_to_label(self.processed_image, self.processed_label, is_result=True))
				self.after(0, lambda: self._enable(self.save_btn, True))
			except Exception as e:
				err_msg = str(e)
				self.after(0, lambda msg=err_msg: messagebox.showerror("Error", f"Background removal failed:\n{msg}"))
			finally:
				self.after(0, self._stop_progress)
				self.after(0, lambda: self._enable(self.open_btn, True))
				self.after(0, lambda: self._enable(self.remove_btn, True))

		# Disable controls and show progress while processing
		self._enable(self.open_btn, False)
		self._enable(self.remove_btn, False)
		self._start_progress()
		threading.Thread(target=work, daemon=True).start()

	def save_result(self):
		if self.processed_image is None:
			messagebox.showinfo("No result", "No processed image to save yet.")
			return

		default_name = "{}_no_bg.png".format(self.original_path.stem if self.original_path else "output")
		initial_dir = str(self.original_path.parent) if self.original_path else str(Path.cwd())
		out_path = filedialog.asksaveasfilename(
			title="Save result",
			defaultextension=".png",
			initialfile=default_name,
			initialdir=initial_dir,
			filetypes=[("PNG", "*.png")],
		)
		if not out_path:
			return

		try:
			self.processed_image.save(out_path, format="PNG")
			messagebox.showinfo("Saved", f"Saved to:\n{out_path}")
		except Exception as e:
			messagebox.showerror("Error", f"Could not save image:\n{e}")

	def clear_images(self):
		self.original_image = None
		self.processed_image = None
		self.original_path = None
		self.original_label.configure(image="")
		self.original_label.image = None
		self.processed_label.configure(image="")
		self.processed_label.image = None
		self._enable(self.remove_btn, False)
		self._enable(self.save_btn, False)

	def _start_progress(self):
		self.progress.start(10)

	def _stop_progress(self):
		self.progress.stop()


def main():
	app = BackgroundRemoverApp()
	app.mainloop()


if __name__ == "__main__":
	main()

