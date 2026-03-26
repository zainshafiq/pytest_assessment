def calculate_cart_total(cart_items, discount=0): 
  if not isinstance(cart_items, list) or not all(isinstance(item, dict) for item in cart_items): 
    raise ValueError("Cart items should be a list of dictionaries.") 

  total = sum(item['price'] * item['quantity'] for item in cart_items) 
  return total * (1 - discount) 
