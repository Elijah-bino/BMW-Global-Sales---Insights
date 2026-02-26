# BMW-Global-Sales

## Aim:
  The main objective of this project is to gain general insight out of data and we will try to answer one main question:
  
    1. Which car is the best performer interms of return on investment?
    
    2. Based on the above outcome, we will analysis if there anything off that we are doing.

## Data:
  Data if fetched from kaggle, link: https://www.kaggle.com/datasets/payaldhokane/bmw-global-sales-and-market-data?resource=download

  Raw data has has 14 columns namely:
  
    1. year
    2. month
    3. country
    4. model - (Vehicle model like i4, 3 series etc)
    5. segment - (says, SUV or sedan)
    6. engine_type - (petrol, hybrid etc)
    7. price_usd
    8. marketing_spend
    9. dealership_count
    10. fuel_price_usd
    11. gdp_growth_percent - (countries GDP)
    12. interest_rate_percent
    13. competition_index - (its a scale which determine how difficult is it to get a sale from 1 to 10)
    14. units_sold

## Tools Used:  
  We are mainly using Python for data wrangling and Tableau for chart representation.  

## Data Wrangling:  
  When exploring data we came across multiple problems:  

  1. Unwanted Columns:
       some of the columns are out of our context namely uel_price_usd, gdp_growth_percent, interest_rate_percent, competition_index; because these         columns won't help us to answer the question we have. So we are removing it to keep the complexity simple.

     <img width="1162" height="276" alt="image" src="https://github.com/user-attachments/assets/a01594a3-29f7-4c22-b7e5-8d307b773583" />

  2. Date is split into different columns:
       As month and year are in two different columns seperately, this is going to create a problem in Tableau, it will read year as date and assign        the column as iether just year alone, otherwise if we make it year-month-day, it will put the default month. To avoide these issues, we are          merging the year and month columns into column date.

      <img width="1314" height="679" alt="image" src="https://github.com/user-attachments/assets/0fde607e-7ab4-4114-b584-3fac4224a96d" />

  3. Error values on column Segment:
       The column segment says if the vehicle is "sedan" or "SUV". but in the initial data we had entries "electric". I did not make any sense as it        is an entry optimal for the colum "engine_type", infact there were the same entries in that column.
     
       <img width="800" height="694" alt="Segment Problem" src="https://github.com/user-attachments/assets/a588b68f-40c8-48ab-bd3e-8b2891ade64c" />

       So we had to change that, for tht we created a map to recognise what each vehicle is, and change all the corresponding entries.
     
       <img width="984" height="938" alt="image" src="https://github.com/user-attachments/assets/cdc3f4ae-fa8c-40ba-b55a-68b53df5c47f" />

  4. Adding column Profit:
     So inorder to answer our quetions, we need a column called profit.
     <img width="1754" height="189" alt="image" src="https://github.com/user-attachments/assets/6639b311-34cb-4025-b83b-9773e129b952" />

  6. Performace vs profit:
     When I was trying to answer our question, a thought came to me, if a product has more margin doesn't mean that it brings in the most revenue.        So the column profit alone couldn't do the job. Therefore I created another column called Sales_Performance.

     <img width="1640" height="782" alt="Creating performance column" src="https://github.com/user-attachments/assets/0207e697-c130-4840-b6a5-019585f9b07a" />

Now the data looks pretty clean, we are jumping to visulaization.

## Tableau - Visuals:  

  The data in imported and all the columns type etc looks good.  

  1. Most units sold:

     <img width="2438" height="804" alt="image" src="https://github.com/user-attachments/assets/5c45056a-10b1-47e9-bc22-368c832c5a63" />

     Turns out X3 hass the highest sales globaly with an average selling price of 76,072 USD.

  2. Sales by engine type:
      <img width="2381" height="1329" alt="image" src="https://github.com/user-attachments/assets/89ce8c48-dfe9-4960-b889-a2ae0a4e9ffc" />

     Electric vehicles and quitely dominating the future world!
     
  4. Models with Dealers:
      <img width="2353" height="1335" alt="image" src="https://github.com/user-attachments/assets/1d35c6fe-db4f-46f5-8697-ee127e74a9bd" />

     X3 is the most amount of car what the dealers sumulatively holds.


  6. No of dealers in countries:
      <img width="2435" height="1139" alt="image" src="https://github.com/user-attachments/assets/78071f6c-ec6e-4d20-a9c4-799cb85ce5cb" />

     China has the most amount of delaers followed by Australia and Brazil

  8. Best Performing Models:
      <img width="2361" height="1333" alt="image" src="https://github.com/user-attachments/assets/9e71adb8-6376-47ec-af7c-3b080ff63c18" />

     X3 has the most return on investment. (in our context we are only considering marketing spend as investment)

     
  10. Profit by models:
      <img width="2426" height="1323" alt="image" src="https://github.com/user-attachments/assets/9e31337e-612e-4300-aba2-327665acede7" />

      So in sense of profits, X7 has the most followed by 3 series.

      
  12. Sales by country and engine type:
      <img width="2318" height="783" alt="image" src="https://github.com/user-attachments/assets/322ce76a-1aa0-4995-9aae-dcc4abe8db4f" />

      China is leading with petrol engine vehicle sales.

  
  14. Sales by segment:
      <img width="2349" height="1317" alt="image" src="https://github.com/user-attachments/assets/cb98e8d9-3268-471e-b732-cb0975ce086f" />

      Sedan is leading the trend!

     
## Answering Questions:  
    
  1. Which car is the best performer interms of return on investment?

     Inorder to answer this question I have taken a look at the profit first (fig 10), it shows that X7 has the most marginf followed by 3 series.        But as mentioned before in the doc, most margin is not equal to most revenue. So, had a look at Sales_Performance (fig 8), tunrs out that X3         produces the most revenue followed by i4 and 3 series.
    
  3. Based on the above outcome, we will analysis if there anything off that we are doing.

     Taking performing models into context, from fig 4, the most model held by delaers are X3, 3 series and i4. But from fig 8, it is clear that i4       contributes more to the revenue than 3 series. It is better to push i4 more.

  
## Insights:  
BMW's global sales performance reveals the X3 SUV as the standout performer across multiple dimensions. It leads in total units sold worldwide (approximately 73,358 units across the dataset), delivers the highest return on marketing investment (treating marketing spend as the primary cost proxy), and generates the strongest overall profit contribution among all models, driven by robust volume and a competitive average selling price of ~$76,072. China emerges as the single largest market by sales volume, followed by the UK and France, yet the number of dealerships in the UK and France is significantly lower than in China. This suggests considerable untapped potential in those two countries — increasing dealership presence there could help capture more market share and accelerate growth. While sedans currently lead in aggregate segment volume, electric powertrains are already dominating by engine type, signaling a clear shift toward electrification. Geographically, China also boasts the highest average number of dealerships, reinforcing its position as the pivotal growth engine, with Australia and Brazil following in dealer network size. The X7, despite lower unit volume, ranks first in total profit thanks to its premium pricing.  

Overall, the data underscores a strong portfolio where the versatile X3 drives volume and marketing efficiency, high-end models like the X7 maximize profit per unit, and electric variants position BMW well for the future — with strategic expansion of dealerships in high-sales, low-dealer markets like the UK and France offering a clear opportunity to further strengthen momentum.












  


























  
