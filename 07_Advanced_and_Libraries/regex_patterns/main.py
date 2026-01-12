import re

text = "The quick brown fox jumps over 13 lazy dogs."
pattern = r"\d+"
print(re.findall(pattern, text))

email_text = "Contact us at support@devfredx.com or info@domain.com.tr"
email_pattern = r"[\w\.-]+@[\w\.-]+"
emails = re.findall(email_pattern, email_text)
print(emails)

phone_text = "Phone numbers: 555-010-9988, 555-123-4455"
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(phone_pattern, phone_text)
print(phones)

html_content = "<div><p>Hello World</p></div>"
clean_text = re.sub(r"<.*?>", "", html_content)
print(clean_text)

data = "user:devfredx;pass:12345;ip:192.168.1.1"
split_data = re.split(r"[;:]", data)
print(split_data)

log = "ERROR: Unauthorized access from 10.0.0.5 at 2026-01-12"
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
print(re.findall(ip_pattern, log))

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", log)
if match:
    print(match.group(0))
    print(match.group(1))

hex_code = "Color code is #FFA500"
print(re.findall(r"#[0-9A-Fa-f]{6}", hex_code))

search_result = re.search(r"^The", text)
if search_result:
    print("Starts with 'The'")

case_check = "Python is cool"
print(re.findall(r"python", case_check, re.IGNORECASE))

multi_line = "First\nSecond\nThird"
print(re.findall(r"^\w+", multi_line, re.MULTILINE))