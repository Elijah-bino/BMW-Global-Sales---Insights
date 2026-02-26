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



























  


























  
