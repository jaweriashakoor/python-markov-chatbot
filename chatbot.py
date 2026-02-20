import numpy as np
import re
import time
from collections import deque

class MarkovBot:
    def __init__(self, file_path):
        self.memory = deque(maxlen=5)
        self.lookup_dict = {}
        self.lookup_dict_1st = {}
        self.train(file_path)

    def train(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_text = f.read().lower()
            
            # Clean data: preserves apostrophes in words like "can't"
            words = re.findall(r"[\w']+|[.!?]", raw_text)
            
            for i in range(len(words) - 1):
                w1, w2 = words[i], words[i+1]
                
                # 1st Order Map
                if w1 not in self.lookup_dict_1st:
                    self.lookup_dict_1st[w1] = []
                self.lookup_dict_1st[w1].append(w2)
                
                # 2nd Order Map
                if i < len(words) - 2:
                    w3 = words[i+2]
                    state = (w1, w2)
                    if state not in self.lookup_dict:
                        self.lookup_dict[state] = []
                    self.lookup_dict[state].append(w3)
        except Exception as e:
            print(f"[ERROR] Failed to index dataset: {e}")

    def generate_response(self, user_input, max_length=20):
        self.memory.append(user_input.lower())
        
        # Select seed word from recent context
        seed_word = None
        all_context = " ".join(list(self.memory))
        context_words = re.findall(r"\b\w+\b", all_context)
        
        for word in reversed(context_words):
            if word in self.lookup_dict_1st:
                seed_word = word
                break
        
        if not seed_word:
            seed_word = np.random.choice(list(self.lookup_dict_1st.keys()))

        # Start sequence
        second_word = np.random.choice(self.lookup_dict_1st[seed_word])
        response = [seed_word, second_word]

        # 2nd Order Generation
        for _ in range(max_length):
            state = (response[-2], response[-1])
            if state in self.lookup_dict:
                next_word = np.random.choice(self.lookup_dict[state])
                response.append(next_word)
                if next_word in ".!?":
                    break
            else:
                break
                
        # Format grammar
        output = " ".join(response).capitalize()
        output = re.sub(r'\s+([.!?])', r'\1', output)
        return output

def run_interface():
    # Configuration
    DATASET_PATH = 'alice.txt'
    
    print("\n" + "="*40)
    print("      ALICE MARKOV INTERFACE [v2.0]")
    print("="*40)
    print(f"[*] Loading dataset: {DATASET_PATH}")
    
    bot = MarkovBot(DATASET_PATH)
    
    print("[+] Model mapping complete.")
    print("[!] Enter 'exit' or 'quit' to end session.")
    print("-" * 40)

    while True:
        try:
            user_msg = input("\nUser > ")
            
            if user_msg.lower() in ['quit', 'exit', 'stop']:
                print("\n[Process Terminated: User Exit]")
                break
            
            if not user_msg.strip():
                continue

            # Artificial delay for human-like feel
            print("Thinking...", end="\r")
            time.sleep(0.4)
            
            reply = bot.generate_response(user_msg)
            print(f"Bot > {reply}")
            
        except KeyboardInterrupt:
            print("\n\n[Forced Shutdown]")
            break

if __name__ == "__main__":
    run_interface()