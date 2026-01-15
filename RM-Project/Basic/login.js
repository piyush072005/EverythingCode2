const email = document.querySelector('#login-email');
const password = document.querySelector('#login-password');

// Only run on the login page (other pages also load this script).
if (email && password) {
  const form = email.closest('form');
  const button = form?.querySelector('button') || form?.querySelector('input[type="submit"]');

  // Create or reuse an error box to avoid duplicates.
  let errorBox = form.querySelector('.login-error');
  if (!errorBox) {
    errorBox = document.createElement('div');
    errorBox.className = 'login-error';
    errorBox.style.color = '#d33';
    errorBox.style.fontWeight = '600';
    errorBox.style.marginTop = '8px';
    errorBox.hidden = true;
    form.appendChild(errorBox);
  }

  const setError = (message) => {
    errorBox.textContent = message;
    errorBox.hidden = !message;
  };

  const setLoading = (isLoading) => {
    if (!button) return;
    button.disabled = isLoading;
    button.dataset.label = button.dataset.label || button.textContent;
    button.textContent = isLoading ? 'Signing in...' : button.dataset.label;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');

    const emailValue = email.value.trim();
    const passwordValue = password.value;

    if (!emailValue || !passwordValue) {
      setError('Email and password are required.');
      return;
    }

    setLoading(true);

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: emailValue, password: passwordValue })
      });

      if (!response.ok) {
        const body = await response.json().catch(() => ({}));
        const message = body.message || 'Invalid credentials';
        throw new Error(message);
      }

      const data = await response.json().catch(() => ({}));
      if (data && data.token) {
        localStorage.setItem('fm_token', data.token);
      }

      window.location.href = 'apply.html';
    } catch (error) {
      setError(error.message || 'Unable to sign in. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Support both clicking the button and pressing Enter.
  if (form) {
    form.addEventListener('submit', handleSubmit);
  }
  if (button) {
    button.addEventListener('click', handleSubmit);
  }
}