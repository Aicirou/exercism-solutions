def is_paired(text):
    text = "".join(item for item in text if item in "()[]{}")
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text