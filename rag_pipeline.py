def get_context(documents):
    """Combine retrieved documents into the context shown to the user."""
    return "\n\n".join(document.page_content for document in documents)