# webScrap

This Python project scraps product titles and reviews / comments from eBay product pages. The script extracts the product title and associated comments or reviews and saves the results to an outputs.txt file.
- **Only tested for ebay, will likely require modification to beautiful soup parsing logic to work for other websites as HTML structure varies**

## Features

- **Collect Data**: Scraps data from provided eBay product URLs with Beautiful Soup.
- **Parse and Extract Title**: Extracts the product title for each URL.
- **Extract Reviews**: Retrieves all review comments and stores them.
- **Save Output**: Writes product titles and reviews to a specified file, **overwriting it with each execution.**

## Installation

1. Ensure that Python 3.x is installed.
2. To set up the environment and dependencies for this project, create a Conda environment using the `requirements.yaml` file provided:

    ```bash
    conda env create -f requirements.yaml
    ```
    This will install all the necessary dependencies, including Python 3.11, BeautifulSoup, and other related libraries.

3. **Do not forget to activate the conda environment if not already activated**

    ```bash
    conda activate webScrap
    ```

## Usage

1. **Prepare Your URL File**: Create a text file named `products.txt` or use the one provided in the project directory with each eBay product URL on a new line.
2. **Run the Script**:

    ```bash
    python webScrap.py
    ```

   The script will:
   - Read URLs from `products.txt`.
   - Scrap the product title and comments for each URL.
   - Save the results in `outputs.txt`.

### Example

#### Input (products.txt):
    https://www.ebay.com/itm/166978620935?_skw=iphone+16&epid=12071671652&itmmeta=01JB2HBYGG0M3W0D7SBEJSR29C&hash=item26e0b38e07%3Ag%3A7UcAAOSw77Rm7ahp&itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKnDmXPHAVQLiIl7HcUektIJ0e3OJolbqXxJ3aV9PQcjFBfmiO0d7U0JmEX0jM6GqQ83ZkGCg1D6HSOqHfN8CRQfVa%2Bdin%2F2SUTNTXd%2BY7XVXTqMTeFcoEBDlDMo6JQ0cdn49NowPM81njrNOB2%2BE%2BLTdbmSKU8ILsWZWI8%2FLb%2FlrvTrHNodwZjmO5e4mTM4iuSnp9FRauid6P1uz1bBXIgqAv7gFrxC17pVSsMLpyMFQA%3D%3D%7Ctkp%3ABk9SR6zor9HYZA&var=466676685842
    https://www.ebay.com/itm/355685944723?_skw=iphone+15&itmmeta=01JB2HEEN1TXGKH9C0DZCJHR5V&hash=item52d088cd93%3Ag%3AhYQAAOSwAhJmNRwt&itmprp=enc%3AAQAJAAAA4HoV3kP08IDx%2BKZ9MfhVJKlhBKQihESsjLwsJw9IgOmb%2BYyW0Q4WhcH0oXmOBbv0wkOFFZqeRfJyu%2Bavh4YvjOpduiUH%2BWXx3nsBsDg%2F7YfC5ASJ%2FWP2HXy924BScA6B0Zs4bXcZUlwYBn8J8dnT5YSW%2Bpj2LmfvPS3AlgmtZLYxm6kk5WLcY4iUuWfGE0TZGIQeVRDScH%2Fh9ENmew9jfjWYpaGMLVStfTkoTD8GCMyMhledzPh8Fa354%2FAtV3Y8UeLmV9NeiTRGbFKEoVEJY2r3n%2F3PsMZwFRU339QUDfix%7Ctkp%3ABk9SR9DqudHYZA&var=624783780301
    https://www.ebay.com/itm/226378094526?_skw=iphone+14&epid=17071608951&itmmeta=01JB2HFA2KHQ4PG89Z9PE0HDTG&hash=item34b52f97be:g:rC4AAOSwl4Jm-t1n&itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKmlmKz1mhZs3Cq2%2B2AVlzZcg8svfKd5MkbCxkBuvB0ijpz762PTHl33efFDLkYYqSRiRGu11E1ex%2FbS7kpE9HHztCeOiq%2FxrAIlQ%2FzlqDbhw5bNG450B%2F6G%2Fz2z8d8dvZmDiQyqywAn9gKILK9SVnAtfBuYG%2BHIMPYpAroAynVAqrzfzyrE8PCfz%2BLCCj1hiQxzBtC9qy%2Fox1RKZ9rrMYAV1kwg%2BXGEZ3jnV9mc3HeuBw%3D%3D%7Ctkp%3ABlBMULChvdHYZA
    https://www.ebay.com/itm/364027692443?_skw=iphone+13&epid=10049287446&itmmeta=01JB2HGNKTJ1R5CGH28QZN8792&hash=item54c1bdc59b%3Ag%3AV7EAAOSwbhFjLLxB&itmprp=enc%3AAQAJAAAA4HoV3kP08IDx%2BKZ9MfhVJKk9sw9rsh5DhJEB1dzyJtbFDFxUitpw1uIX6b3%2FYNen0oY1Ci4hGKT--%2F9P9WkJtPkR0Eam6qWvKmhQg%2B10YgiQ%2Bz48YFh6C4943q4EkfObzJXhOnjIVmlmDVSUKuM733nDmkoUkvth16eSdz8XdOMdSI%2B0uXKZCjXUKYmv6K24okXENbwxPIQIRar9qOKeDRG%2Bq9Kf4uVSRwzqWzNZ78kmEOJ%2BmhiTEs5vbnC%2Fkts9OVPUVUTTHm22R8or%2FUZfbjsNxnPSkt5omrv0HXhne%2BQG%7Ctkp%3ABFBM_tnC0dhk&var=633337981704
    https://www.ebay.com/itm/384501272640?_skw=iphone+12&epid=12041705134&itmmeta=01JB2HGY81EJ7QCG0KF0RFF1SE&hash=item59860fd040%3Ag%3AngcAAOSwy9RhkpBT&itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKlO%2FX28bCwvOhRSYnX0TmCcOxH9KvQmHNW19ClVYQuc8%2Ft9NGDce6Co8A%2BJ00rUDsAoo7R%2F9EyXb1c3JNCW2h54I3eiiDuaeHZIq2VxITOklHt%2FgYIZUM8y6Ppw7jh%2FgBXmcSLPWo4%2B7bqodo3A5UIekx6R652uxB%2BSqjnaikuvFgAVekQkwz9n0lnKa5glYnfGErq6%2BSGbB16PXprIW6E1kuTiQHRClyC779mR67Bb0A%3D%3D%7Ctkp%3ABk9SR5Dkw9HYZA&var=652602897249


#### Output (outputs.txt)
    Apple - iPhone 16 - 256gb - Factory Sealed - Factory Warranty - UNLOCKED
    Comment 1: Very Fast Shipper, Excellent Product & Price. 
    Comment 2: excelente  producto muy recomendado 
    Comment 3: Fast shipping thanks!!
    Comment 4: Item came exactly as described, no issues! Once ordered, it was quickly shipped. The product was open box but nothing was missing and even the box still looked undamaged, all items and accessories were within box. Price was also unbeatable compared to other sellers who had used/new items much more expensive than what I paid. Overall happy and satisfied with purchase, thank you seller!
    Comment 5: 2nd Purchased from seller: Great communication, Great packaging and great price. Item descriptions 100%. I will buy again. Thank You,
    Comment 6: This item came a day early. The seller and decent communication. The item’s condition was about true to the  description. Overall a good seller and I do recommend.
    
    ----------------------------------------------------------------------------------------------------
    
    Apple iPhone 15 Pro 256GB Unlocked Excellent Condition
    Comment 1: Item arrived quickly.  In very nice shape cosmetically.  All set up and working fine.  Battery charge capacity 100%.
    Comment 2: Very good quality item for good price!!!
    Comment 3: A++ supplier, phone in like new condition. Great transaction. 
    Comment 4: Phone shipped out fast was in good condition like mentioned in the description my only issue was the price I purcahsed the phone 1 day and the very next day the phone price had dropped about $80 I reached out to the seller but couldn't come to a solution that bestvsuited me, but overall the seller was quick in their response so I'll give them a plus in that department I'd purchase again as well.
    Comment 5: The phone works well and looks as good as described. Shipping was fast and arrived by predicted date. Overall the purchase was a pleasant experience. I don't know what else needs to be said. I didn't communicate with the buyer because there was no need to.  Phone was packaged well for shipping. This is starting to feel like homework just to leave a positive feedback why must I reach 500 characters? eBay do better.
    Comment 6: Product arrived quickly and well packaged. Exactly as described, working perfectly. Great communication with the seller and excellent service. Highly recommend!
    
    ----------------------------------------------------------------------------------------------------
    
    Unlocked Apple iPhone 14 Pro Max 256 GB  Deep Purple Excellent Condition GSM
    Comment 1: I sent a message to the seller prior to my order getting here the seller responded very quickly and was very understanding, patient. I just received my package it had tiny bit of wear and tear but overall almost in pristine condition i am very happy with my purchase also it got here very quickly and was packaged very nicely with lots of bubble wrap. I definitely will be checking out what else this seller has listed and if I find something I would definitely buy from again thank you so Much!!!
    Comment 2: Didn't pull anything major but got 14 draft picks & plenty of mega stars. I'm happy with this overall transaction. it is a great product at a very fair price. Package store and Speedy Delivery earns this transaction and easy five-☆☆☆☆☆.  I recommend this seller very highly. I'll be back. 
    Comment 3: A++++ Ebayer,fast shipping,excellent packing,great communication. Pulled some nice cards thanks very much for the great deal. Highly recommend 
    
    ----------------------------------------------------------------------------------------------------
    
    Apple iPhone 13 Pro Max 128GB Unlocked Smartphone -Excellent
    Comment 1: Used this seller before. Very happy with the purchase. Phone is almost a 10 some minor minor scratches. One area on the screen and after I put a glass protector on it looks perfect. Phone reports repair of camera and display. Says reported to apple with genuine Apple components. Pricing was reasonable and seems to function flawlessly. Battery capacity shows 90%. Super fast shipping. The 13 pro max is maybe the best model ever produced if you research it. One thing I like is physical sim and esim
    Comment 2: Dont hesistate to buy this product, Iphone 13 pm came in excellent condition with one tiny insignificant chip on top of phone which i only noticed underneath direct light at a certain angle (which doesn't matter because of using a case) Battery health was at an excellent 96%. IMEI checks out and overall im very satisfied as this was my first refurbished Iphone purchased on ebay and not through apples overpriced program. Thank you to the seller. 
    Comment 3: Absolutely flawless device. Battery health is at 100% and I've checked over and over and there is not a single scratch, or even a sign of ever being used. I feel like this is literally a brand-new phone. Shipping was fast and overall, a great product!
    Comment 4: Received promptly, carefully packaged. Pristine condition, looks almost like new! Love the purple! Battery life acceptable with description. Seamless set up with my carrier. Have used for past month without any problems. Very pleased! Came with charging cord as described. Recommend seller! 
    Comment 5: I never received the iPhone still now and the packed is marked untracked. I contacted the seller and he or she responded to my messages only twice and ignored me. I recently opened a refund claim with ebay. I think this seller is not trustworthy. 
    Comment 6: Ordered phone but returned due to battery health being 82% when advertised minimum of 85%. Replacement phone came with 84%. Decided to keep it. Overall good seller with great communication. Phone is near mint condition
    
    ----------------------------------------------------------------------------------------------------
    
    Apple iPhone 12 Pro Max 128GB Unlocked Smartphone - Excellent
    Comment 1: I received the phone very quickly. Phone is in excellent condition! No noticeable damage, scratches or wear.  Setup was quick.  Only been using for 4 days, and I haven’t had any issues so far. Very pleased. Battery life was 87 as stated which is still considered good for this phone. Very satisfied with this purchase. Recommend this seller definitely.
    Comment 2: Item was as advertised excellent condition no scratches. Was easily able to connect to my carrier. The only complaint I have is that the battery health is at 87% that should have been in the description or a price drop but other than that. I recommend buying from this seller
    Comment 3: I love the iphone 12pro max even it's looks old, everything is perfect and excellent, and only comes with cable without adaptor, thanks 
    Comment 4: Received promptly, carefully packaged. Pristine condition, looks almost like new! Love the purple! Battery life acceptable with description. Seamless set up with my carrier. Have used for past month without any problems. Very pleased! Came with charging cord as described. Recommend seller! 
    Comment 5: I never received the iPhone still now and the packed is marked untracked. I contacted the seller and he or she responded to my messages only twice and ignored me. I recently opened a refund claim with ebay. I think this seller is not trustworthy. 
    Comment 6: Ordered phone but returned due to battery health being 82% when advertised minimum of 85%. Replacement phone came with 84%. Decided to keep it. Overall good seller with great communication. Phone is near mint condition
    
    ----------------------------------------------------------------------------------------------------
    
    

## Code Structure

- **collectData(url)**: Sends an HTTP GET request to the provided URL and returns a BeautifulSoup object for parsing.
- **analyzeData(soup, url)**: Parses the BeautifulSoup object to extract the product title and comments.
- **main()**: Coordinates execution of processes

## Requirements

This project uses the following dependencies, which can be installed via `requirements.yaml`:

- Python 3.x
- requests
- BeautifulSoup4 (bs4)
- lxml

## License

This project is licensed under the MIT License.
