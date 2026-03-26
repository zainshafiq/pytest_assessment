def validate_shipping_address(address):
  required_fields = ['name', 'street', 'city', 'postcode', 'country'] 
  if not isinstance(address, dict): 
    raise ValueError("Address must be a dictionary.") 
  
  missing_fields = [field for field in required_fields if field not in address] 
  
  if missing_fields: 
    raise ValueError(f"Missing required fields: {', '.join(missing_fields)}") 
    
  return True
