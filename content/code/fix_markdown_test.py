import re
def fix_markdown_links(text):
    # Fix broken link format
    text = re.sub(r'\s*"?\s*target\s*=\s*"?\s*blank"?\s*', '', text, flags=re.IGNORECASE)
    
    # Convert HTML links to Markdown format
    text = re.sub(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>', r'[\2](\1)', text, flags=re.IGNORECASE)
    
    return text

# Test cases
test_cases = [
    "[paid host](http://www.hostrocket.com/\" target=\"blank)",
    "<a href=\"http://x10hosting.com/\" target=\"blank\">free host</a>"
]

for case in test_cases:
    print(f"Before: {case}")
    print(f"After: {fix_markdown_links(case)}")
    print()
