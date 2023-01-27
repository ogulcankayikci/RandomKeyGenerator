import random
import string

def generate_random_string():
    # Rastgele büyük harfler ve sayılar için karakter setleri
    letters_and_numbers = string.ascii_uppercase + string.digits
    
    # Rastgele beş bölüm oluşturma
    sections = []
    for i in range(5):
        section = ""
        for i in range(5):
            section += random.choice(letters_and_numbers)
        sections.append(section)
    
    # Bölümleri birleştirme ve "-" koyma
    random_string = "-".join(sections)
    return random_string

print(generate_random_string())
