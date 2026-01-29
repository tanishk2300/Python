# Given a dictionary of products and their prices, find the product with the highest price.
product={"powder":"2000","senitiser":"3000","perfume":"4000","eno":"5000"}

highest_product=max(product,key=product.get)
print("product with highest price",highest_product,"=",product[highest_product])
