# Payout scraper
Payout scraper shows the prices we can get for a specific shoe on various sales platforms connected to discord for better use.  
I made the project to save time because checking it manually takes a lot of time.

At the moment, the scraper works on the following websites:  
- Stockx.com (the user can choose the seller level and currency, unfortunately I don't have access to the endpoint that shows the prices of business accounts, so this feature is not working for now)
- Sneakit.com

# How to set up scraper
- Login into discoord developer portal and create a bot and copy the token (https://discord.com/developers/docs/intro).
- Add bot to specified server.
- Paste the token to main.py file (last line of code).
- Add proxies to proxy.txt file.
- Run main.py

# Commands
- Stockx:
    > ```!user``` Seller_level Currency Account_type
    - Sets/Updates user information, takes the following values (if something go wrong bot will send embed):
      - Seller_level: 1, 2, 3, 4, 5 
      - Currency: gbp, eur, usd
      - Account_type: private, business (doesnt work at the moment)  
    <br>
    
  > ```!stockx``` sku
  - Shows payout information for specified sku
  <br>
  
  > ```!sx``` sku
  - Shows payout information for specified sku (mobile friendly)
  <br>
  
  > ```info```
  - Shows current user information
  <br>

- Sneakit:
    > ```!sneakit``` sku
    - Shows payout information for specified sku
    <br>
    
  > ```!kit``` sku
  - Shows payout information for specified sku (mobile friendly)
  <br>
  
 # TODO
   - Add sales platform named klekt.com []
   - Add sales platform named hypeboost.com []
   - Work with the second stockx's endpoint to find the query string to the lowest asks in the business account []

 # Additional information
   - Square brackets in the lowest ask column in the stockx module mean that there is no lowest ask for a given size and the price is taken from the highest bid.
   - For hosting scraper 24/7 I recommend using heroku.com because it's cheap and hassle-free.
  
 # Images
  <img src="https://user-images.githubusercontent.com/115949757/208200542-2a0d4526-3128-4773-b91a-5e0983581c19.png" width="500">  
  <img src="https://user-images.githubusercontent.com/115949757/208200595-03b9167c-c743-4435-b954-ea715da3b989.png" width="500">  
  <img src="https://user-images.githubusercontent.com/115949757/208200642-6825f38a-a7f6-4a93-98e5-51cfbe0c2d03.png" width="500">  
  <img src="https://user-images.githubusercontent.com/115949757/208200595-03b9167c-c743-4435-b954-ea715da3b989.png" width="500">    
  <img src="https://user-images.githubusercontent.com/115949757/208200686-fccfec7f-7296-4959-8c42-219f11d027ae.png" width="500">    
  <img src="https://user-images.githubusercontent.com/115949757/208200825-bbffc839-7596-4907-93ea-5787ab73d2ef.png" width="500">  
