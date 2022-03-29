from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, col
# from database import db_config as cfg
# import db_config as cfg 
# import models as mdl
from models import ExpenditurePayee, Filer, ExpenditureFiler, Expenditure, ContributionFiler, Contribution, ErrorLog
from db_config import DbConfig
from datetime import datetime
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore

engine = db_engine = DbConfig.get_central_engine()
             

class UpdateExpenditureFiler:
    header_text = None
    def __init__(self, org_id, header_text=None, status_id=None):
        self.org_id = org_id
        self.header_text = header_text
        self.status_id = status_id
        
    def text(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == self.org_id)
            results = session.exec(statement)
            filer = results.one()
            # print("ExpenditureFiler:", filer.filer_name)
            # print(header_text)
            filer.tweet_header_text = self.header_text
            filer.text_update_dt = datetime.now()        
            session.add(filer)
            session.commit()           
            
    def tweeted_id(self):
        with Session(engine) as session:
            statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == self.org_id)
            results = session.exec(statement)
            filer = results.one()
            # print("ExpenditureFiler:", filer.filer_name)
            # print(header_text)
            filer.tweet_header_id = self.status_id
            filer.text_tweeted_dt = datetime.now()
            session.add(filer)
            session.commit()            
 
class UpdateContributionFiler:
    def __init__(self, org_id, header_text=None, status_id=None):
        self.org_id = org_id  
        self.header_text = header_text
        self.status_id = status_id
                
    def text(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).where(ContributionFiler.org_id == self.org_id)
            results = session.exec(statement)
            filer = results.one()
            # print("Hero:", filer)

            filer.tweet_header_text = self.header_text
            filer.text_update_dt = datetime.now()
            session.add(filer)
            session.commit()        

    def tweeted_id(self):
        with Session(engine) as session:
            statement = select(ContributionFiler).where(ContributionFiler.org_id == self.org_id)
            results = session.exec(statement)
            filer = results.one()
            # print("Hero:", filer)

            filer.tweet_header_id = self.status_id
            filer.text_tweeted_dt = datetime.now()        
            session.add(filer)
            session.commit()  

class UpdateExpenditure:
    def __init__(self, expenditure_id, tweet_text=None, status_id=None, replied_to_status_id=None):
        self.expenditure_id = expenditure_id
        self.tweet_text = tweet_text
        self.status_id = status_id
        self.replied_to_status_id = replied_to_status_id        
        
    def update_text(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id == self.expenditure_id).where(Expenditure.expenditure_id != 6760)
            results = session.exec(statement)
            expenditure = results.one()
            # print("ExpenditureFiler:", expenditure.filer_name, expenditure.expenditure_amount)
            # print(tweet_text)
            expenditure.tweet_message = self.tweet_text
            expenditure.tweet_message_update_dt = datetime.now()
            session.add(expenditure)
            session.commit()   
            
    def update_tweeted(self):
        with Session(engine) as session:
            statement = select(Expenditure).where(Expenditure.expenditure_id == self.expenditure_id)
            results = session.exec(statement)
            expenditure = results.one()
            # print("ExpenditureFiler:", expenditure.filer_name, expenditure.expenditure_amount)
            # print(tweet_text)
            expenditure.tweet_sent_text = self.tweet_text
            expenditure.tweet_id = self.status_id
            expenditure.tweet_sent = 1
            expenditure.tweet_dt = datetime.now()
            expenditure.replied_to_status_id = self.replied_to_status_id
            session.add(expenditure)
            session.commit() 
            session.refresh(expenditure)             
                  
class UpdateContribution:
    def __init__(self, receipt_id, tweet_text=None, status_id=None, replied_to_status_id=None):
        self.receipt_id = receipt_id
        self.tweet_text = tweet_text  
        self.status_id = status_id
        self.replied_to_status_id = replied_to_status_id
              
    def update_text(self):
        with Session(engine) as session:
            statement = select(Contribution).where(Contribution.receipt_id == self.receipt_id)
            results = session.exec(statement)
            contribution = results.one()
            # print("ExpenditureFiler:", contribution.filer_name, contribution.receipt_amount)
            # print(tweet_text)
            contribution.tweet_message = self.tweet_text
            contribution.tweet_message_update_dt = datetime.now()
            session.add(contribution)
            session.commit()  
            session.refresh(contribution)              
                
    def update_tweeted(self):
        with Session(engine) as session:
            # print('attempting to update tweeted contribution')
            statement = select(Contribution).where(Contribution.receipt_id == self.receipt_id)
            results = session.exec(statement)
            contribution = results.one()

            contribution.tweet_sent_text = self.tweet_text
            contribution.tweet_id = self.status_id
            contribution.tweet_sent = 1
            contribution.tweet_dt = datetime.now()
            contribution.replied_to_status_id = self.replied_to_status_id        
            session.add(contribution)
            session.commit()
            session.refresh(contribution)  
        
        # session.close()            
 

 
        
        
class InsertErrorLog:
    def __init__(self,error_message):
        self.error_message = error_message
        pass        
    def insert_error_log(self):
        with Session(engine) as session:
            error = ErrorLog(
                error_message = str(self.error_message)
            )
            session.add(error)
            session.commit()
            session.close()                        
        
class PayeeStuffFixLater:
    def __init__(self):
        pass        
    # def insert_expenditure_payee(payee_in):
    #     with Session(engine) as session:
    #         payee = payee_in
    #         try:
    #             print(payee)       
    #             session.add(payee)
    #         except Exception as e:
    #             insert_error_log(str(e))
    #             pass       
    #         try:
    #             session.commit()
    #         except Exception as e:
    #             insert_error_log(str(e))            
    #             pass
    #         session.close()      

# def select_expenditure_payee(payee_name_in):

    # def build_expenditure_payee(payee_name_in, payee_type_in,last_name_in,first_name_in,middle_name_in
    #                             # ,address_1_in,address_2_in,city_in,state_in,zip_in
    #                             ):
    #     with Session(engine) as session:
    #         payee = ExpenditurePayee(payee_type = payee_type_in,
    #                                 payee_name = payee_name_in,
    #                                 last_name = last_name_in,
    #                                 first_name = first_name_in,
    #                                 middle_name = middle_name_in,
    #                                 # address_1 = address_1_in,
    #                                 # address_2 = address_2_in,
    #                                 # city = city_in,
    #                                 # state = state_in,
    #                                 # zip = zip_in 
    #                                 )

    #     return payee

def main():
    pass
  
      
                
if __name__ == "__main__":
    main()

