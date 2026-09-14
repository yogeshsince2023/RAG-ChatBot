def get_context(documents):
    """Combine retrieved documents into the context shown to the user."""
    return "\n\n".join(document.page_content for document in documents)


def answer_query(documents, query, max_sentences=3):
    """Return the most relevant sentences from the retrieved document context."""
    query_words = {
        word.lower()
        for word in query.split()
        if len(word) > 2
    }
    sentences = []
    for document in documents:
        for sentence in document.page_content.replace("\n", " ").split("."):
            sentence = sentence.strip()
            if sentence:
                words = set(sentence.lower().split())
                score = len(query_words & words)
                sentences.append((score, sentence))

    ranked = sorted(sentences, key=lambda item: item[0], reverse=True)
    selected = [sentence for score, sentence in ranked[:max_sentences] if score > 0]
    return ". ".join(selected) + ("." if selected else "No direct answer was found in the uploaded PDF.")