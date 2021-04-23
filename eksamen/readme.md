# Eksamensprojekt

## Jörgs forslag
## Stage 1: Business Case Foundation

1. Collect ideas and define a business or social domain, where data science can bring a value.
2. Search Internet and get inspired by sources of information, related to your ideas.
3. Formulate context, purpose, questions, and hypotheses for a data science experiment.
4. Technology
    - Select and install software tools and development environments.
    - Create a Github repository, which will host all project components during all stages of the development and implementation process.
    - Create and upload a .md file as an initial release of the project, which contains brief 
    annotation of your ideas, in minimum four sentences, telling:
        - what is in the focus of your interest?
            - Cryptocurrencies and the impact on todays market. Is it something that will stay forever, or is it just something that will disappear if we all lost interest in it?

            **We would say it will stay on the market and will maybe be the future currency!!!**

            One reason for that assumption is that you will be able to cut the middleman. With that I mean the bank that will take a cut of every transaction you may be doing in the future. Think about all the people who sends money from Europe, every month to Turkey, Phillipiens, China and so on. They all have to pay a fee for transfering there hard earned money to a bank or two. It also will take as much as 3-6 days before the other hands will recieve there money. With cryptcurrency it will be an instant transfer with minimum or none fee.
        - why is it interesting?
            - Cryptocurrency has been on the market for quite a while now. It started out to be a thing only for nerds, where as today more and more investers are trying there luck with the new currency. Some of the big guys are, Musk (1,5 billion $ in BitCoin), MicroStrategy(3 billion $ in BitCoin) [Link](https://decrypt.co/47061/public-companies-biggest-bitcoin-portfolios) and the list goes on. But not only big players are on the market, also ordinary folks are investing into cryptocurrencies. The reason for this could be that those big investers, are seen some kind of insurrence. Its also very easy to start trading the currency. You only thing you have to do is sign up for one the of dozen cryptocurrency trading markets and you good to go in ca 2 hours. 
            One of the two biggest trade platforms Coinbase and Crypto.com gives you even the possibility to get a VISA card and pay with your card in restaurants, shops, where- ever VISA is aloud to be used. But you will not be paying with DKk, dollars or euros but with your cryptocurrency. For just that matter Crypt.com created even there own currency called cryptocoin.  
        - which outcome do you expect from your research?
            - more and more ordinary people will invest
            - it will show that the currency will stay on for a long time
        - who may be a user of the results?
            - if you have money lying in your bank account, it will do you nothing good. It may even get less, because of inflation. Why not having your money work for you instead given it to your bank coin by coin. There are also lot of people who thought about getting into the trading game, but where to frightend to invest there money in something as versatile as shares. 
            Our research could eliminate maybe some of the fright about cryptocurrency. Some of the frights are: 1. is the currency legit 2. will it stay on..
           
## Mads forslag  
  Trading platform med flg. egenskaber:  
   * Kurs predicter - en komponent der trækker kursdata på aktier, (crypto)valutaer, råstoffer mv. og forudsiger kursudviklingen vha. ML.  
   * Status calculator - en komponent der scraper artikler fra konfigurerbare kilder og beregner disses score vha. ML (positiv/negativ).  
   Scraper resultater gemmes evt. i graph database eller lign. db til store datamængder (HBase?).  
   Skal kunne udlede relevante søgekriterier fra de scrapede artikler og scrape videre indtil en vis dybde er nået.
  * De 2 ovenstående komponenter skal samlet give en anbefaling om køb/salg af f.eks. værdipapirer.
  * Nice-to-have: Autotrade modul.
## Claus forslag  
  Fraud detection - en komponent der scraper f.eks. DBA og på baggrund af diverse kriterier kan forudsige om en given annonce er snyd.
  - Kriterier kunne være:
    - (Konfigurerbare)
    - Område
    - Beløb
    - Type af vare
    - Tlf. nr (antal øvrige annoncer, taletid mv.)
    - Evt. sammenkædning med data om rapporter om snyd fra Politi/DBA mv. (nok svært at få fat i.)
    - Genbrug af billeder (kræver db)
