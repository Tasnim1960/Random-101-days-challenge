import hashlib
import random
import string
from datetime import datetime

def generate_digital_dna(name):
    # Current timestamp
    now = datetime.now().strftime("%Y%m%d%H%M%S%f")
    
    # Random salt
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    # Combine everything
    raw_data = name + now + salt
    
    # Create hash
    dna = hashlib.sha256(raw_data.encode()).hexdigest()
    
    # Format nicely
    unique_id = f"{dna[:8]}-{dna[8:16]}-{dna[16:24]}"
    
    return unique_id

# Example
user_name = input("Enter your name: ")
print("Your Digital DNA ID:", generate_digital_dna(user_name))