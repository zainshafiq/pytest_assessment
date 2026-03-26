def apply_discounts(cart_total, discount_codes): 
  valid_discounts = {'SAVE10': 0.10, 'SAVE20': 0.20, 'SAVE50': 0.50} 
  total_discount = 0
  
  for code in discount_codes: 
    if code not in valid_discounts: 
      raise ValueError(f"Invalid discount code: {code}") 
    if total_discount + valid_discounts[code] > 1: 
      raise ValueError("Total discount cannot exceed 100%.") 
    total_discount += valid_discounts[code] 
    
  return cart_total * (1- total_discount)
