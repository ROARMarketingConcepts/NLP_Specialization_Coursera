
def basic_hash_table(value_1,n_buckets): 

    def hash_function (value_1,n_buckets):
        return int(value_1) % n_buckets

    hash_table = {i:[] for i in range(n_buckets)}
    
    for value in value_1:
        hash_value = hash_function(value,n_buckets)
        hash_table[hash_value].append(value)
    
    return hash_table