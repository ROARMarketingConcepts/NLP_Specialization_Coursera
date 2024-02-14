def side_of_plane(P,v):
    dotproduct = np.dot(P,v.T) # Get the dot product P * v'
    sign_of_dot_product = np.sign(dotproduct) # The sign of the elements of the dotproduct matrix 
    sign_of_dot_product_scalar = sign_of_dot_product.item() # The value of the first item
    return sign_of_dot_product_scalar


def hash_multiple_plane(P_1,v):

	hash_value = 0

	for i, P in enumerate (P_1):
		sign = side_of_plane(P,v)
		hash_i = 1 if sign >=0 else 0
		hash_value += 2**i*hash_i

	return hash_value
