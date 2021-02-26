# Farmers-Market

```
+--------------|--------------|---------+
| Product Code |     Name     |  Price  |
+--------------|--------------|---------+
|     CH1      |   Chai       |  $3.11  |
|     AP1      |   Apples     |  $6.00  |
|     CF1      |   Coffee     | $11.23  |
|     MK1      |   Milk       |  $4.75  |
|     OM1      |   Oatmeal    |  $3.69  |
+--------------|--------------|---------+
```

This week, we’re celebrating our one year anniversary and would like to offer the
following specials.  To do so, we’ll need to update our checkout system to apply
the following rules.

1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples

At any time, we are able to print out the current register to see what the state of
the basket is.  This will include the price and the applied discount or special, if any.

# Running the Program with Docker - Instructions

In your command prompt/terminal,

1. Clone the repo
```
git clone https://github.com/ethanchen7/Farmers-Market.git
```

2. Build the docker image (note the period (".") after "instance")
```
cd Farmers-Market
docker build -t instance .
```
3. Run the container
```
docker run -it --rm instance
```
4. Test out the program!
