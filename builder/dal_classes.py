# from crypt import methods
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, or_
# import db_config as cfg
# import models as mdl
from models import ExpenditurePayee, Filer, ExpenditureFiler, Expenditure, ContributionFiler, Contribution, ErrorLog
from db_config import DbConfig
from sqlmodel.sql.expression import Select, SelectOfScalar
from rich import inspect

engine = db_engine = DbConfig.get_central_engine()
    
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore       
    
class SelectExpenditures:
       
    def __init__(self,amount=None):
        self.amount = amount
        # self.org_id = org_id
        # self.expenditure_id              
        pass
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt()) 
    
    def all_greater_than(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_amount >= self.amount).order_by(Expenditure.expenditure_amount.desc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures     
    
    def all(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures        
    
    def all(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures 
        
    def tweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.tweet_sent == 1).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures          
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.tweet_sent == 0).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures  
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Expenditure).where(Expenditure.tweet_message == None).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures  

    def all_ids():
        with Session(engine) as session:
            statement = select(Expenditure.expenditure_id).where(Expenditure.expenditure_id != 6760)
            results = session.exec(statement)
            rtn_results = results.fetchall() 
        return rtn_results 

class SelectOrgExpenditures:
    def __init__(self,org_id):
        self.org_id = org_id
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt())    
    
    def last_tweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.org_id == self.org_id).where(Expenditure.tweet_id != None).order_by(Expenditure.tweet_dt.desc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results          
    
    def all(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.org_id == self.org_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures 
        
    def tweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.tweet_sent == 1).where(Expenditure.org_id == self.org_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures          
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.tweet_sent == 0).where(Expenditure.org_id == self.org_id).where(Expenditure.expenditure_id != 6760).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures  
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Expenditure).where(Expenditure.tweet_message == None).where(Expenditure.org_id == self.org_id).order_by(Expenditure.expenditure_date.asc())
            results = session.exec(statement)
            expenditures = results.fetchall() 
            return expenditures           
        
class SelectSingleExpenditure:
    
    def __init__(self, expenditure_id):
        self.expenditure_id = expenditure_id
        
    def __str__(self):
        exp = self.get_expenditure()
        string = ''
        string += f"filer_name: {exp.expenditure_id}" + '\r\n'        
        string += f"filer_name: {exp.filer_name}" + '\r\n'
        string += f"amt: {exp.expenditure_amount}" + '\r\n'
        string += f"payee: {exp.payee_name}" + '\r\n'
        string += f"exp_date: {exp.expenditure_date}"    
        return string
    
    def get(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id == self.expenditure_id).where(Expenditure.expenditure_id != 6760)
            results = session.exec(statement)
            # print(dir(results))
            expenditure = results.first() 
            return expenditure 
    
class SelectContributions:
    def __init__(self):              
        pass
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt()) 
    
    def all(self):
        with Session(engine) as session:
            statement = select(Contribution).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.tweet_sent == 0).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions   
        
    def tweeted(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.tweet_sent == 1).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions    
        
        
    def last_tweeted(self):
        with Session(engine) as session:
            statement = (select(Contribution) 
                .where(Contribution.tweet_sent == 1) 
                .where(Contribution.tweet_id !="1506004750164185090") 
                .where(Contribution.tweet_id !="1506004903574966272") 
                .where(Contribution.tweet_id !="1506005056985853957") 
                .where(Contribution.tweet_id !="1506005210023731201") 
                .where(Contribution.tweet_id !="1506005362637369347") 
                .order_by(Contribution.tweet_id.desc())
            )
            results = session.exec(statement)
            contributions = results.first() 
            return contributions              
                        
            
    def first_tweeted(self):
        with Session(engine) as session:
            statement = (select(Contribution) 
                .where(Contribution.tweet_sent == 1) 
                .where(Contribution.tweet_id !="1506004750164185090") 
                .where(Contribution.tweet_id !="1506004903574966272") 
                .where(Contribution.tweet_id !="1506005056985853957") 
                .where(Contribution.tweet_id !="1506005210023731201") 
                .where(Contribution.tweet_id !="1506005362637369347") 
                .order_by(Contribution.tweet_id.asc())
            )                                                                                                        
            results = session.exec(statement)
            contributions = results.first() 
            return contributions         
                
    # def last_tweeted(self):
    #     with Session(engine) as session:
    #         statement = select(Contribution).where(Contribution.tweet_sent == 1).order_by(Contribution.receipt_date.asc())
    #         results = session.exec(statement)
    #         contributions = results.fetchall() 
    #         return contributions                    
        
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Contribution).where(Contribution.tweet_message == None).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions
          
    def all_ids():
        with Session(engine) as session:
            statement = select(Contribution.receipt_id)
            results = session.exec(statement)
            rtn_results = results.fetchall() 
        return rtn_results                
    
class SelectSingleContribution:
    def __init__(self, receipt_id):
        self.receipt_id = receipt_id
    
    def __str__(self):
        con = self.get()
        string = ''
        string += f"contr_id: {con.receipt_id}" + '\r\n'        
        string += f"filer_name: {con.filer_name}" + '\r\n'
        string += f"org_id: {con.org_id}" + '\r\n'
        string += f"amt: {con.receipt_amount}" + '\r\n'
        string += f"payor: {con.payor_name}" + '\r\n'
        string += f"rcp_date: {con.receipt_date}"    
        return string
    
    def get(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.receipt_id== self.receipt_id)
            results = session.exec(statement)
            # print(dir(results))
            expenditure = results.first() 
            return expenditure     
  
class SelectSingleContribtionTweetText:
    def __init__(self, tweet_text):
        self.tweet_text = tweet_text
    
    def __str__(self):
        con = self.get()
        string = ''
        string += f"contr_id: {con.receipt_id}" + '\r\n'        
        string += f"filer_name: {con.filer_name}" + '\r\n'
        string += f"org_id: {con.org_id}" + '\r\n'
        string += f"amt: {con.receipt_amount}" + '\r\n'
        string += f"payor: {con.payor_name}" + '\r\n'
        string += f"rcp_date: {con.receipt_date}"    
        return string
    
    def get(self):
        with Session(engine) as session:
            statement = select(Contribution).filter(self.tweet_text in Contribution.tweet_message)
            results = session.exec(statement)
            # print(dir(results))
            expenditure = results.first() 
            return expenditure       
  
  
  
class SelectOrgContributions:
    def __init__(self, org_id):              
        self.org_id = org_id
    
    def count_all(self):
        return len(self.all())
    
    def count_untweeted(self):
        return len(self.untweeted())
    
    def count_unbuilt(self):
        return len(self.unbuilt()) 
    
    def last_tweeted(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_dt.desc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results
    
    def last_status_id(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_id.desc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results  
    
    def first_status_id(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_id.asc())
            results = session.exec(statement)
            rtn_results = results.first() 
        return rtn_results          
    
    def all(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.org_id == self.org_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.tweet_sent == 0).where(Contribution.org_id == self.org_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions   
        
    def unbuilt(self):
        with Session(engine) as session:    
            statement = select(Contribution).where(Contribution.tweet_message == None).where(Contribution.org_id == self.org_id).order_by(Contribution.receipt_date.asc())
            results = session.exec(statement)
            contributions = results.fetchall() 
            return contributions

      
  
class SelectContributionFilers:
    def __init__(self):
        pass
    
    def count(self):
        return len(self.all())
    
    def all(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).order_by(ContributionFiler.receipt_count.desc())
            results = session.exec(statement)
            # print(dir(results))
            filers = results.fetchall()
            # for filer in results:
            #     print(filer.org_id)
            return filers   
        
    def unbuilt(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).where(ContributionFiler.tweet_header_text == None)
            results = session.exec(statement)
            # print(dir(results))
            filers = results.fetchall()
            # for filer in results:
            #     print(filer.org_id)
            return filers           

    def untweeted(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).where(ContributionFiler.tweet_header_id == None)
            results = session.exec(statement)            
            filers = results.fetchall()    
            return filers          
        
        
class SelectExpenditureFilers:
    def __init__(self):
        pass
    
    def count(self):                        
        return len(self.all())
    
    def all(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers 
        
    # def all_test(self):
    #     with Session(engine) as session:
    #         statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == 7626)
    #         results = session.exec(statement)
    #         filers = results.fetchall()
    #         return filers      
        
    def all_test(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(or_(
                                                           ExpenditureFiler.org_id == 7397,                
                                                           ExpenditureFiler.org_id == 7417,
                                                           ExpenditureFiler.org_id == 7582,
                                                           ExpenditureFiler.org_id == 7688,
                                                           ExpenditureFiler.org_id == 7626,
                                                           ExpenditureFiler.org_id == 7491,
                                                           ExpenditureFiler.org_id == 7579,
                                                           ExpenditureFiler.org_id == 7339,
                                                           ExpenditureFiler.org_id == 7680,                                                         
                                                           ExpenditureFiler.org_id == 7347,
                                                           ExpenditureFiler.org_id == 7694,
                                                           ExpenditureFiler.org_id == 7432
                                                           )
                                                       )
            results = session.exec(statement)
            filers = results.fetchall()
            return filers                 
        
    def unbuilt(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.tweet_header_text == None)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers 

    def untweeted(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.tweet_header_id == None)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers    
        
    def untweeted(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.tweet_header_id == None)
            results = session.exec(statement)
            filers = results.fetchall()
            return filers                                  
           
    
class SelectContributionFiler:
    def __init__(self, org_id):
        self.org_id = org_id
     
    def __str__(self):
        filer = self.get()
        string = ''
        string += f"org_id: {filer.org_id}" + '\r\n'
        string += f"name: {filer.filer_name}"
        return string
        
    def get(self):
        try:
            with Session(engine) as session:
                statement = select(ContributionFiler).where(ContributionFiler.org_id == self.org_id)
                results = session.exec(statement)
                # print(dir(results))
                filer = results.one()
                # for filer in results:
                #     print(filer.org_id)
                return filer
        except: 
            return None     

class SelectExpenditureFiler:
    def __init__(self, org_id):
        self.org_id = org_id
     
    def __str__(self):
        filer = self.get()
        string = ''
        string += f"org_id: {filer.org_id}" + '\r\n'
        string += f"name: {filer.filer_name}"
        return string
        
    def get(self):
        try:
            with Session(engine) as session:
                statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == self.org_id)
                results = session.exec(statement)
                # print(dir(results))
                filer = results.one()
                # for filer in results:
                #     print(filer.org_id)
                return filer
        except: 
            return None    
    
class SelectFiler:
    def __init__(self):
        # self.org_id = org_id
        pass
     
    def __str__(self):
        filer = self.get()
        string = ''
        string += f"org_id: {filer.org_id}" + '\r\n'
        string += f"name: {filer.filer_name}"
        return string
        
    def all(self):
        try:
            with Session(engine) as session:
                statement = select(Filer)
                results = session.exec(statement)
                # print(dir(results))
                filers = results.fetchall()
                # for filer in results:
                #     print(filer.org_id)
            return filers
        except Exception as e:
            raise
            # return None       
    
    
      
def main():
    x = SelectContributions()
    last = x.last_tweeted()
    first = x.first_tweeted()
    print('last', last.tweet_id)
    print('first', first.tweet_id)
    
    
  
  
  
  
  
  
  
#         results = session.exec(statement)
#         # print(dir(results))
#         filers = results.fetchall()
#         # for filer in results:
#         #     print(filer.org_id)
#         return filers  
    
# def select_contribution_filers_all():
#     with Session(engine) as session:
#         statement = select(ContributionFiler)
#         results = session.exec(statement)
#         # print(dir(results))
#         filers = results.fetchall()
#         # for filer in results:
#         #     print(filer.org_id)
#         return filers       
    
    
# def select_expenditure_filer(org_id):
#     with Session(engine) as session:
#         statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == org_id)
#         results = session.exec(statement)
#         # print(dir(results))
#         filer = results.one()
#         # for filer in results:
#         #     print(filer.org_id)
#         return filer 
        
        
# def select_contribution_filer(org_id):
#     with Session(engine) as session:
#         statement = select(ContributionFiler).where(ContributionFiler.org_id == org_id)
#         results = session.exec(statement)
#         # print(dir(results))
#         filer = results.one()
#         # for filer in results:
#         #     print(filer.org_id)
#         return filer         
    
# def select_single_filer(org_id):
#     with Session(engine) as session:
#         statement = select(Filer).where(Filer.org_id == org_id)
#         results = session.exec(statement)
#         # print(dir(results))
#         filer = results.first()
#         # for filer in results:
#         #     print(filer.org_id)
#         return filer  
    
# def select_expenditures_all():
#     with Session(engine) as session:
#         statement = select(Expenditure)
#         results = session.exec(statement)
#         # print(dir(results))
#         expenditures = results.fetchall() 
#         return expenditures 
    
    
# def select_contributions_all():
#     with Session(engine) as session:
#         statement = select(Contribution)
#         results = session.exec(statement)
#         # print(dir(results))
#         contribution = results.fetchall() 
#         return contribution      
  
# def select_single_expenditure(expenditure_id):
#     with Session(engine) as session:
#         statement = select(Expenditure).where(Expenditure.expenditure_id == expenditure_id)
#         results = session.exec(statement)
#         # print(dir(results))
#         expenditure = results.first() 
#         return expenditure 
    
# def select_single_contribution(receipt_id):
#     with Session(engine) as session:
#         statement = select(Contribution).where(Contribution.receipt_id == receipt_id)
#         results = session.exec(statement)
#         # print(dir(results))
#         contribution = results.first() 
#         return contribution     


# def select_expenditures_by_org(org_id, unsent_only):
#     with Session(engine) as session:
#         if unsent_only:
#             statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_sent == 0).order_by(Expenditure.expenditure_date.asc())
#         else: 
#             statement = select(Expenditure).where(Expenditure.org_id == org_id).order_by(Expenditure.expenditure_date.asc())
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results


# def select_contributions_by_org(org_id, unsent_only):
#     with Session(engine) as session:
#         if unsent_only:
#             statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_sent == 0).order_by(Contribution.receipt_date.asc())
#         else: 
#             statement = select(Contribution).where(Contribution.org_id == org_id).order_by(Contribution.receipt_date.asc())
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results

  
# def select_last_expenditure_tweetid_by_org(org_id):
#     with Session(engine) as session:
#         statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_id != None).order_by(Expenditure.tweet_dt.desc())
#         results = session.exec(statement)
#         rtn_results = results.first() 
#     return rtn_results  

# def select_last_contribution_tweetid_by_org(org_id):
#     with Session(engine) as session:
#         statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_dt.desc())
#         results = session.exec(statement)
#         rtn_results = results.first() 
#     return rtn_results

# def update_expenditure_tweet_header(org_id, header_text):
#     with Session(engine) as session:
#         statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == org_id)
#         results = session.exec(statement)
#         filer = results.one()
#         # print("ExpenditureFiler:", filer.filer_name)
#         # print(header_text)
#         filer.tweet_header_text = header_text
#         session.add(filer)
#         session.commit()
        
# def update_contribution_tweet_header(org_id, header_text):
#     with Session(engine) as session:
#         statement = select(ContributionFiler).where(ContributionFiler.org_id == org_id)
#         results = session.exec(statement)
#         filer = results.one()
#         # print("Hero:", filer)

#         filer.tweet_header_text = header_text
#         session.add(filer)
#         session.commit()        


# def update_expenditure_tweet_text(expenditure_id, tweet_text):
#     with Session(engine) as session:
#         statement = select(Expenditure).where(Expenditure.expenditure_id == expenditure_id)
#         results = session.exec(statement)
#         expenditure = results.one()
#         # print("ExpenditureFiler:", expenditure.filer_name, expenditure.expenditure_amount)
#         # print(tweet_text)
#         expenditure.tweet_message = tweet_text
#         session.add(expenditure)
#         session.commit()
        
        
# def update_contribution_tweet_text(receipt_id, tweet_text):
#     with Session(engine) as session:
#         statement = select(Contribution).where(Contribution.receipt_id == receipt_id)
#         results = session.exec(statement)
#         contribution = results.one()
#         # print("ExpenditureFiler:", contribution.filer_name, contribution.receipt_amount)
#         # print(tweet_text)
#         contribution.tweet_message = tweet_text
#         session.add(contribution)
#         session.commit()  
        
        
# def update_sent_expenditure_tweet(expenditure_id,status_id, tweet_text):
#     with Session(engine) as session:
#         statement = select(Expenditure).where(Expenditure.expenditure_id == expenditure_id)
#         results = session.exec(statement)
#         expenditure = results.one()
#         # print("ExpenditureFiler:", expenditure.filer_name, expenditure.expenditure_amount)
#         # print(tweet_text)
#         expenditure.tweet_sent_text = tweet_text
#         expenditure.tweet_id = status_id
#         session.add(expenditure)
#         session.commit()  


# def update_sent_contributor_tweet(receipt_id,status_id, tweet_text):
#     with Session(engine) as session:
#         statement = select(Contribution).where(Contribution.receipt_id == receipt_id)
#         results = session.exec(statement)
#         contribution = results.one()

#         contribution.tweet_sent_text = tweet_text
#         contribution.tweet_id = status_id
#         session.add(contribution)
#         session.commit()
#         # session.close()            
 
  
 
    
# def select_expenditure_payee_distinct():
#     with Session(engine) as session:
#         statement = select(Expenditure.payee_or_recipient_or_in_kind_contributor_type, 
#                            Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
#                            Expenditure.first_name, 
#                            Expenditure.middle_name
#                         #    Expenditure.address_1,
#                         #    Expenditure.address_2,
#                         #    Expenditure.city,
#                         #    Expenditure.state,
#                         #    Expenditure.zip
                           
#                            ).distinct()
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results
# class SelectExpenditurePayee:
#     def __init__(self):
#         kwargs = kwargs        
#         pass
    
#     def names_distinct():
#         with Session(engine) as session:
#             statement = select(
#                             Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
#                             Expenditure.first_name, 
#                             Expenditure.middle_name
#             ).distinct()
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#         return rtn_results
    
#     def names_addresses_disinct():
#         with Session(engine) as session:
#             statement = select(        
#                            Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
#                            Expenditure.first_name, 
#                            Expenditure.middle_name,
#                            Expenditure.address_1,
#                            Expenditure.address_2,
#                            Expenditure.city,
#                            Expenditure.state,
#                            Expenditure.zip,
#                            Expenditure.expenditure_date 
#             ).distinct()
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#         return rtn_results   
                   
#     def names_type_distinct():
#         with Session(engine) as session:
#             statement = select(        
#                            Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
#                            Expenditure.first_name, 
#                            Expenditure.middle_name,
#                         #    Expenditure.address_1,
#                         #    Expenditure.address_2,
#                         #    Expenditure.city,
#                         #    Expenditure.state,
#                         #    Expenditure.zip,
#                            Expenditure.expenditure_date 
#             ).distinct()
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#         return rtn_results                      
            
# def select_expenditure_payee_name_distinct():
#     with Session(engine) as session:
#         statement = select(
#                         #    Expenditure.payee_or_recipient_or_in_kind_contributor_type, 
#                            Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
#                            Expenditure.first_name, 
#                            Expenditure.middle_name
#                         #    Expenditure.address_1,
#                         #    Expenditure.address_2,
#                         #    Expenditure.city,
#                         #    Expenditure.state,
#                         #    Expenditure.zip
                           
#                            ).distinct()
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results        
# def select_contribution_contributor_distinct():
#     with Session(engine) as session:
#         statement = select(Contribution.contributor_or_transaction_source_type, 
#                            Contribution.contributor_or_source_name_individual_last_name, 
#                            Contribution.first_name, 
#                            Contribution.middle_name,
#                            Contribution.address_1,
#                            Contribution.address_2,
#                            Contribution.city,
#                            Contribution.state,
#                            Contribution.zip                           
#                            ).distinct()
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results   

# class InsertErrorLog:
#     def insert_message(error_message_in):
#         with Session(engine) as session:
#             error = ErrorLog(
#                 error_message = error_message_in            
#             )
#             session.add(error)
#             session.commit()
#             session.close()

# class InsertExpenditurePayee:         
#     def insert_payee(self, payee_in):
#         with Session(engine) as session:
#             payee = payee_in
#             try:
#                 print(payee)       
#                 session.add(payee)
#             except Exception as e:
#                 InsertErrorLog.insert_message(str(e))
#                 pass       
#             try:
#                 session.commit()
#             except Exception as e:
#                 InsertErrorLog.insert_message(str(e))            
#                 pass
#             session.close()      

# def select_expenditure_payee(payee_name_in):

# def build_expenditure_payee(payee_name_in, payee_type_in,last_name_in,first_name_in,middle_name_in
#                             # ,address_1_in,address_2_in,city_in,state_in,zip_in
#                             ):
#     with Session(engine) as session:
#         payee = ExpenditurePayee(
#                                 original_payee_name = payee_name_in,
#                                 payee_name = '',
#                                 last_name = '',
#                                 first_name = first_name_in,
#                                 middle_name = middle_name_in,
#                                 # address_1 = address_1_in,
#                                 # address_2 = address_2_in,
#                                 # city = city_in,
#                                 # state = state_in,
#                                 # zip = zip_in 
#                                 )

#     return payee

# def main():
#     # insert_error_log(error_message_in='this is an error message')
#     SelectExpenditurePayee.names_distinct()
    # payee = SelectExpenditurePayee.names_distinct()
    # # InsertExpenditurePayee.insert_payee(payee_in=payee)
    # # [build_expendture_payee(x) for x in select_expenditure_payee_distinct]
    # for x in payee:
    #     # payee = build_expenditure_payee(x)
    #     print(payee)
        # original_payee_name = x.payee_or_recipient_or_in_kind_contributor_name
        # last_name = x.payee_or_recipient_or_in_kind_contributor_name
        # first_name = x.first_name
        # middle_name = x.middle_name
  
        # if payee_type == 'Individual':
        #     if middle_name != None:
        #         payee_name = last_name + ', ' + first_name + ' ' + middle_name
        #         payee = build_expenditure_payee(payee_name_in=payee_name, e,last_name_in=last_name,first_name_in=first_name,middle_name_in=middle_name
        #                                         # ,address_1_in=address_1,address_2_in=address_2,city_in=city,state_in=state,zip_in=zip
        #                                         )
        #         InsertExpenditurePayee.insert_payee(payee_in=payee)
        #     elif middle_name == None:
        #         payee_name = last_name + ', ' + first_name
        #         payee = build_expenditure_payee(payee_name_in=payee_name, payee_type_in=payee_type,last_name_in=last_name,first_name_in=first_name,middle_name_in=''
        #                                         # ,address_1_in=address_1,address_2_in=address_2,city_in=city,state_in=state,zip_in=zip
        #                                         )
        #         InsertExpenditurePayee.insert_payee(payee_in=payee)
        # if payee_type != 'Individual':
        #     payee = build_expenditure_payee(payee_name_in=payee_name, payee_type_in=payee_type,last_name_in='',first_name_in='',middle_name_in=''
                                            # ,address_1_in=address_1,address_2_in=address_2,city_in=city,state_in=state,zip_in=zip
                                            # )
            # InsertExpenditurePayee.insert_payee(payee_in=payee)
            


      
if __name__ == "__main__":
    main()
    
# def build_expendture_payee(payee_name, payee_type,last_name,first_name,middle_name,address_1,address_2,city,state,zip):
#     payee = ExpenditurePayee(payee_name = f"""{payee_name}""",
#                             payee_type = f"""{payee_type}""",    
#                             last_name = f"""{last_name}""",
#                             first_name = f"""{first_name}""",
#                             middle_name = f"""{middle_name}""",
#                             address_1 = f"""{address_1}""",
#                             address_2 = f"""{address_2}""",
#                             city = f"""{city}""",
#                             state = f"""{state}""",
#                             zip = f"""{zip}""" )
#     # print(payee.payee_name)
    
    
    
    # [print(x) for x in payee]
    # select_expenditures()  
    
    # results = select_filers_all().where
    # results = select_filers_all()            
    # for filer in results:
    #         print(filer.org_id)
    
    
    # filers = select_contribution_filers_all()
    # [print(x.filer_name) for x in filers]
    
    # filers = select_expenditure_filers_all()
    # [print(x.filer_name) for x in filers if len(x.filer_name) > 50]     
    # org_id = 7312
    # # limit_rows = 3
    # unsent_only = True
    
    # x = select_last_contribution_tweetid_by_org(org_id)
    # print(x.tweet_id, x.receipt_id)
    
    # x = select_last_contribution_tweetid_by_org(org_id)
    # print(x.tweet_id, x.receipt_id)    
    # contributions= select_contributions_by_org(org_id=org_id, unsent_only=unsent_only)
   
   
    # contributions= select_contributions_by_org(org_id=org_id, unsent_only=unsent_only)
   
   
    # print(contributions) 
    # [print(x.receipt_date) for x in contributions if x.payee_or_recipient_or_in_kind_contributor_name == 'USPS']
    
    # [print(x.receipt_date, x.contributor_or_source_name_individual_last_name, x.first_name) for x in contributions]   
    
    # org_id = 7494     
    # results = select_filer(org_id)  
    # print(results.org_id) 
    # print(results.filer_type)
    # print(results.filer_name)              
    # for filer in results:
    #         print(filer.org_id)   
    
# def select_expenditures_by_org(org_id, limit_rows, unsent_only):
#     with Session(engine) as session:
#         if int(limit_rows or 0) == 0:
#             if unsent_only == False: 
#                 statement = select(Expenditure).where(Expenditure.org_id == org_id)
#                 results = session.exec(statement)
#                 print(1)
#                 # return results
#             elif unsent_only > True:
#                 statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_sent == 0)
#                 results = session.exec(statement)
#                 print(2)
#                 # return results
#         elif int(limit_rows or 0) > 0:
#             if unsent_only == False: 
#                 statement = select(Expenditure).where(Expenditure.org_id == org_id).limit(limit_rows)
#                 results = session.exec(statement)
#                 print(3)
#                 # return results
#             elif unsent_only == True:
#                 statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_sent == 0).limit(limit_rows)        
#                 results = session.exec(statement)
#                 print(4)
#                 # return results
#         # print(dir(results))
#         # return results
#         rtn_results = results.fetchall() 
#     return rtn_results

  
# def select_contributions_by_org(org_id, limit_rows, unsent_only):
#     with Session(engine) as session:
#         if int(limit_rows or 0) == 0:
#             if unsent_only == False: 
#                 statement = select(Contribution).where(Contribution.org_id == org_id)
#                 results = session.exec(statement)
#                 print(1)
#                 # return results
#             elif unsent_only > True:
#                 statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_sent == 0)
#                 results = session.exec(statement)
#                 print(2)
#                 # return results
#         elif int(limit_rows or 0) > 0:
#             if unsent_only == False: 
#                 statement = select(Contribution).where(Contribution.org_id == org_id).limit(limit_rows)
#                 results = session.exec(statement)
#                 print(3)
#                 # return results
#             elif unsent_only == True:
#                 statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_sent == 0).limit(limit_rows)        
#                 results = session.exec(statement)
#                 print(4)
#                 # return results
#         # print(dir(results))
#         # return results
#         contributions = results.fetchall() 
#     return contributions               