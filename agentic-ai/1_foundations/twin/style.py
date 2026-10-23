"""Reusable styling and interface settings for the digital-twin Gradio chatbot."""

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
    color-scheme: light;
    --twin-page: #ffffff;
    --twin-surface: #ffffff;
    --twin-panel-border: #e5e7eb;
    --twin-text: #202123;
    --twin-muted: #6b7280;
    --twin-user-bg: #eff6ff;
    --twin-user-border: #bfdbfe;
    --twin-user-text: #1e3a8a;
    --twin-assistant-bg: #f0fdf4;
    --twin-assistant-border: #86efac;
    --twin-assistant-text: #14532d;
    --twin-accent: #10a37f;
    --twin-input-focus: #93c5fd;
}

/* Gradio's theme toggle adds the dark class to the document body. */
body.dark,
html.dark {
    color-scheme: dark;
    --twin-page: #111318;
    --twin-surface: #191c23;
    --twin-panel-border: #343a46;
    --twin-text: #e5e7eb;
    --twin-muted: #9ca3af;
    --twin-user-bg: #172554;
    --twin-user-border: #3b82f6;
    --twin-user-text: #dbeafe;
    --twin-assistant-bg: #052e16;
    --twin-assistant-border: #16a34a;
    --twin-assistant-text: #dcfce7;
    --twin-accent: #34d399;
    --twin-input-focus: #60a5fa;
}

html,
body,
gradio-app {
    background: var(--twin-page) !important;
    color: var(--twin-text) !important;
}

.gradio-container {
    width: 100% !important;
    max-width: 860px !important;
    min-width: 0 !important;
    margin: 0 auto !important;
    background: var(--twin-page) !important;
    color: var(--twin-text) !important;
}

.chat-header {
    max-width: 760px;
    margin: 0 auto !important;
    padding: 2.5rem 1rem 1.25rem !important;
    background: transparent !important;
    border: 0 !important;
    box-shadow: none !important;
    text-align: center;
}

.chat-header h1 {
    margin: 0 0 0.5rem;
    color: var(--twin-text) !important;
    font-size: clamp(1.8rem, 5vw, 2.35rem) !important;
    font-weight: 600 !important;
    letter-spacing: -0.035em !important;
}

.chat-header p {
    margin: 0;
    color: var(--twin-muted) !important;
    font-size: 1rem;
}

#karan-chatbot {
    max-width: 760px;
    margin: 0 auto;
    overflow: hidden;
    border: 1px solid var(--twin-panel-border) !important;
    border-radius: 1.25rem !important;
    background: var(--twin-surface) !important;
    box-shadow: 0 8px 28px rgb(17 24 39 / 6%) !important;
}

#karan-chatbot [data-testid="user"] {
    box-sizing: border-box;
    padding: 0.9rem 1.15rem !important;
    border: 1px solid var(--twin-user-border) !important;
    border-radius: 1.25rem 1.25rem 0.35rem 1.25rem !important;
    background: var(--twin-user-bg) !important;
    color: var(--twin-user-text) !important;
    -webkit-text-fill-color: var(--twin-user-text) !important;
    box-shadow: 0 2px 8px rgb(37 99 235 / 8%);
}

#karan-chatbot [data-testid="user"] * {
    color: var(--twin-user-text) !important;
    -webkit-text-fill-color: var(--twin-user-text) !important;
}

#karan-chatbot [data-testid="bot"] {
    box-sizing: border-box;
    padding: 0.9rem 1.15rem !important;
    border: 2px solid var(--twin-assistant-border) !important;
    border-left: 5px solid var(--twin-accent) !important;
    border-radius: 1.25rem 1.25rem 1.25rem 0.35rem !important;
    background: var(--twin-assistant-bg) !important;
    color: var(--twin-assistant-text) !important;
    -webkit-text-fill-color: var(--twin-assistant-text) !important;
    box-shadow: 0 2px 8px rgb(16 163 127 / 7%);
}

#karan-chatbot [data-testid="bot"] * {
    color: var(--twin-assistant-text) !important;
    -webkit-text-fill-color: var(--twin-assistant-text) !important;
}

#karan-input {
    width: 100%;
    max-width: 760px;
    margin: 0.75rem auto 1rem;
    border: 1px solid var(--twin-user-border) !important;
    border-radius: 1.5rem !important;
    background: var(--twin-user-bg) !important;
    box-shadow: 0 2px 10px rgb(37 99 235 / 8%) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

#karan-input textarea,
#karan-input textarea:focus {
    box-sizing: border-box;
    padding: 0.9rem 1.15rem !important;
    background: var(--twin-user-bg) !important;
    color: var(--twin-user-text) !important;
    -webkit-text-fill-color: var(--twin-user-text) !important;
    caret-color: var(--twin-user-text) !important;
}

#karan-input textarea::placeholder {
    color: var(--twin-muted) !important;
    -webkit-text-fill-color: var(--twin-muted) !important;
    opacity: 1;
}

#karan-input:focus-within {
    border-color: var(--twin-input-focus) !important;
    box-shadow: 0 0 0 3px rgb(59 130 246 / 12%),
        0 2px 10px rgb(37 99 235 / 8%) !important;
}

[data-testid="examples"] {
    background: transparent !important;
}

[data-testid="examples"] button {
    min-height: 0 !important;
    padding: 0.7rem 0.9rem !important;
    border: 1px solid var(--twin-panel-border) !important;
    border-radius: 0.75rem !important;
    background: var(--twin-surface) !important;
    color: var(--twin-text) !important;
    text-align: left !important;
    text-transform: none !important;
    letter-spacing: normal !important;
}

[data-testid="examples"] button:hover {
    border-color: var(--twin-accent) !important;
}

button {
    transition: background-color 0.15s ease, transform 0.15s ease !important;
}

button:hover {
    transform: translateY(-1px);
}

@media (max-width: 640px) {
    .chat-header {
        padding: 1.5rem 0.75rem 0.75rem !important;
    }

    #karan-input {
        margin: 0.5rem 0.25rem 0.75rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
    }
}
"""

JS = """
() => {
  document.title = 'Karan Pratap Singh | Digital Twin';

  const focusInput = () => {
    const textareas = document.querySelectorAll('#karan-input textarea');
    if (textareas.length) textareas[textareas.length - 1].focus();
  };

  setTimeout(focusInput, 300);

  // Restore focus after Gradio re-enables the message field.
  const watchTextarea = (textarea) => {
    if (textarea.dataset.twinWatched) return;
    textarea.dataset.twinWatched = '1';
    let wasDisabled = textarea.disabled || textarea.readOnly;

    new MutationObserver(() => {
      const isDisabled = textarea.disabled || textarea.readOnly;
      if (wasDisabled && !isDisabled) textarea.focus();
      wasDisabled = isDisabled;
    }).observe(textarea, {
      attributes: true,
      attributeFilter: ['disabled', 'readonly'],
    });
  };

  const scanForTextareas = () => {
    document
      .querySelectorAll('#karan-input textarea')
      .forEach(watchTextarea);
  };

  setTimeout(scanForTextareas, 500);
  new MutationObserver(scanForTextareas).observe(document.body, {
    childList: true,
    subtree: true,
  });
}
"""