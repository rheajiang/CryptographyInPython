import hashlib
import time
import sys

max_nonce = 2 ** 32
header = "test block with transaction"
difficulty_bits = 30
target = 2 ** (256 - difficulty_bits)

for nonce in range(max_nonce):
    print(str(nonce)+'\n')
    message = bytes(str(header) + str(nonce), 'utf-8')
    hash_result = hashlib.sha256(message).hexdigest()

    if int(hash_result,16) < target:
        print("Success with nonce %d" % nonce)
        hsb = bin(int(hex(int(hash_result,16)).upper(), 16))
        print("Hash is\n%s" % str(hsb))
        print(bin(target))
        break

print
"Failed after %d(max_nonce) tries" % nonce




'''if __name__ == '__main__':
    difficulty_bits = 5
    new_block = "test block with transaction"
    hash_result = proof_of_work(new_block, difficulty_bits)
    for difficulty_bits in range(5):

        difficulty = 2 ** difficulty_bits

        print
        "Difficulty:%ld(%d bits)" % (difficulty, difficulty_bits)

        print
        "Starubg searching....."

        start_time = time.time()

        new_block = "test block with transaction" + hash_result

        (hash_result, nonce) = (proof_of_work(new_block, difficulty_bits))

        end_time = time.time()

        elapsed_time = end_time - start_time

        print
        "Elapsed_time is %.4f seconds" % elapsed_time

        if elapsed_time > 0:
            hash_power = float(nonce/ elapsed_time)

            print
            "Hashing pwer:%ld hashes per second" % hash_power'''
