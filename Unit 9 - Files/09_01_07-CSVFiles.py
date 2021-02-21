"""
CSV files are plaintext files and therefore easily parsed with Python without additional libraries.
"""

with open('logger.csv') as log_csv_file:
    csv_data = log_csv_file.read()

print(csv_data)

"""
logger.csv

Name,Age,ID
Richard Andrews,43,0de2ecf31df2386377b1d2dc4fae8b16fad05ad0         
Hailey Sellers,24,3d9b8a95458c1df2687191e8146a97ca4afb28aa          
Jessica Pace,39,a5daa63ef893cb86bc8df1110cc9a5f8e1d0c563            
Jasmine Escobar,42,9844e403841ec84b9a2fb3caf9d2a1c9ee042d31         
Karen Kelly,26,8338f76ac0e9a76d73d57790f1d9843b185b5428             
Patricia Christensen,70,23099bb630c1c64989458393045f08de3bac0eb9    
Jessica Hansen,24,a8c035ccd099ef909a46e0d96b76c0f132c9c562          
Raymond Adams,53,a051901830ff6c2095524ef92b1541eef9f8c64d           
Stephanie Morrow,53,3bad04a5fc0a7ec33735ae45535f354887988f35        
Timothy Ramos,34,b4930920b5256c4e592541297e43a556c8fe33a8
"""
