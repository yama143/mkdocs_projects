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
             
def select_filers_all():
    with Session(engine) as session:
        statement = select(Filer)
        results = session.exec(statement)
        # print(dir(results))
        filers = results.fetchall()
        # for filer in results:
        #     print(filer.org_id)
        return filers
    # return results 
    
def select_expenditure_filers_all():
    with Session(engine) as session:
        statement = select(ExpenditureFiler)
        results = session.exec(statement)
        # print(dir(results))
        filers = results.fetchall()
        # for filer in results:
        #     print(filer.org_id)
        return filers  
    
def select_contribution_filers_all():
    with Session(engine) as session:
        statement = select(ContributionFiler)
        results = session.exec(statement)
        # print(dir(results))
        filers = results.fetchall()
        # for filer in results:
        #     print(filer.org_id)
        return filers       
    
    
def select_expenditure_filer(org_id):
    with Session(engine) as session:
        statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == org_id)
        results = session.exec(statement)
        # print(dir(results))
        filer = results.one()
        # for filer in results:
        #     print(filer.org_id)
        return filer 
    
    
# def select_expenditure_all_ids():
#     with Session(engine) as session:
#         statement = select(Expenditure.expenditure_id)
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results 

# def select_contribution_all_ids():
#     with Session(engine) as session:
#         statement = select(Contribution.receipt_id)
#         results = session.exec(statement)
#         rtn_results = results.fetchall() 
#     return rtn_results 
        
def select_contribution_filer_header(org_id):
    try:
        with Session(engine) as session:
            statement = select(ContributionFiler).where(col(ContributionFiler.org_id) == org_id)
            results = session.exec(statement)
            # print(dir(results))
            filer = results.one()
            # for filer in results:
            #     print(filer.org_id)
            return filer
    except: 
        return None    
        
def select_contribution_filer(org_id):
    try:
        with Session(engine) as session:
            statement = select(ContributionFiler).where(col(ContributionFiler.org_id) == org_id)
            results = session.exec(statement)
            # print(dir(results))
            filer = results.one()
            # for filer in results:
            #     print(filer.org_id)
            return filer
    except: 
        return None       
    
def select_single_filer(org_id):
    with Session(engine) as session:
        statement = select(Filer).where(Filer.org_id == org_id)
        results = session.exec(statement)
        # print(dir(results))
        filer = results.first()
        # for filer in results:
        #     print(filer.org_id)
        return filer  
    
def select_contributions_all():
    with Session(engine) as session:
        statement = select(Contribution)
        results = session.exec(statement)
        # print(dir(results))
        contribution = results.fetchall() 
        return contribution       
    
def select_expenditures_all():
    with Session(engine) as session:
        statement = select(Expenditure)
        results = session.exec(statement)
        # print(dir(results))
        expenditures = results.fetchall() 
        return expenditures 
    
def select_contributions_unsent():
    with Session(engine) as session:
        statement = select(Contribution).where(Contribution.tweet_sent == 0).order_by(Contribution.receipt_date.asc())
        results = session.exec(statement)
        rtn_results = results.fetchall() 
        return rtn_results    
        
def select_contributions_unbuilt():
    with Session(engine) as session:        
        statement = select(Contribution).where(Contribution.tweet_message == None).order_by(Contribution.receipt_date.asc())
        results = session.exec(statement)
        rtn_results = results.fetchall() 
        return rtn_results          
 
def select_expenditures_unsent():
    with Session(engine) as session:
        statement = select(Expenditure).where(Expenditure.tweet_sent == 0).order_by(Expenditure.expenditure_date.asc())
        results = session.exec(statement)
        rtn_results = results.fetchall() 
        return rtn_results

def select_expenditures_unbuilt():
    with Session(engine) as session:    
        statement = select(Expenditure).where(Expenditure.tweet_message == None).order_by(Expenditure.expenditure_date.asc())
        results = session.exec(statement)
        rtn_results = results.fetchall() 
        return rtn_results

    
    
   
  
def select_single_expenditure(expenditure_id):
    with Session(engine) as session:
        statement = select(Expenditure).where(Expenditure.expenditure_id == expenditure_id)
        results = session.exec(statement)
        # print(dir(results))
        expenditure = results.first() 
        return expenditure 
    
def select_single_contribution(receipt_id):
    with Session(engine) as session:
        statement = select(Contribution).where(Contribution.receipt_id == receipt_id)
        results = session.exec(statement)
        # print(dir(results))
        contribution = results.first() 
        return contribution     





def select_expenditures_by_org(org_id, unsent_only, only_new):
    with Session(engine) as session:
        if unsent_only:
            statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_sent == 0).order_by(Expenditure.expenditure_date.asc())
        elif only_new:
            statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_message == None).order_by(Expenditure.expenditure_date.asc())
        else: 
            statement = select(Expenditure).where(Expenditure.org_id == org_id).order_by(Expenditure.expenditure_date.asc())
        results = session.exec(statement)
        rtn_results = results.fetchall() 
    return rtn_results


def select_contributions_by_org(org_id, unsent_only,  only_new):
    with Session(engine) as session:
        if unsent_only:
            statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_sent == 0).order_by(Contribution.receipt_date.asc())
        elif only_new:
            statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_message == None).order_by(Contribution.receipt_date.asc())
        else: 
            statement = select(Contribution).where(Contribution.org_id == org_id).order_by(Contribution.receipt_date.asc())
        results = session.exec(statement)
        rtn_results = results.fetchall() 
    return rtn_results

  
def select_last_expenditure_tweetid_by_org(org_id):
    with Session(engine) as session:
        statement = select(Expenditure).where(Expenditure.org_id == org_id).where(Expenditure.tweet_id != None).order_by(Expenditure.tweet_dt.desc())
        results = session.exec(statement)
        rtn_results = results.first() 
    return rtn_results  

def select_last_contribution_tweetid_by_org(org_id):
    with Session(engine) as session:
        statement = select(Contribution).where(Contribution.org_id == org_id).where(Contribution.tweet_id != None).order_by(Contribution.tweet_dt.desc())
        results = session.exec(statement)
        rtn_results = results.first() 
    return rtn_results

# def update_expenditure_tweet_header(org_id, header_text):
#     with Session(engine) as session:
#         statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == org_id)
#         results = session.exec(statement)
#         filer = results.one()
#         # print("ExpenditureFiler:", filer.filer_name)
#         # print(header_text)
#         filer.tweet_header_text = header_text
#         filer.text_update_dt = datetime.now()        
#         session.add(filer)
#         session.commit()
        
# def update_contribution_tweet_header(org_id, header_text):
#     with Session(engine) as session:
#         statement = select(ContributionFiler).where(ContributionFiler.org_id == org_id)
#         results = session.exec(statement)
#         filer = results.one()
#         # print("Hero:", filer)

#         filer.tweet_header_text = header_text
#         filer.text_update_dt = datetime.now()
#         session.add(filer)
#         session.commit()        

# def update_expenditure_tweet_header_status(org_id, status_id):
#     with Session(engine) as session:
#         statement = select(ExpenditureFiler).where(ExpenditureFiler.org_id == org_id)
#         results = session.exec(statement)
#         filer = results.one()
#         # print("ExpenditureFiler:", filer.filer_name)
#         # print(header_text)
#         filer.tweet_header_id = status_id
#         filer.text_tweeted_dt = datetime.now()
#         session.add(filer)
#         session.commit()

# def update_contribution_tweet_header_status(org_id, status_id):
#     with Session(engine) as session:
#         statement = select(ContributionFiler).where(ContributionFiler.org_id == org_id)
#         results = session.exec(statement)
#         filer = results.one()
#         # print("Hero:", filer)

#         filer.tweet_header_id = status_id
#         filer.text_tweeted_dt = datetime.now()        
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
#         expenditure.tweet_message_update_dt = datetime.now()
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
#         contribution.tweet_message_update_dt = datetime.now()
#         session.add(contribution)
#         session.commit()  
        
        



# def update_sent_contribution_tweet(receipt_id,status_id, tweet_text, replied_to_status_id):
#     with Session(engine) as session:
#         statement = select(Contribution).where(Contribution.receipt_id == receipt_id)
#         results = session.exec(statement)
#         contribution = results.one()

#         contribution.tweet_sent_text = tweet_text
#         contribution.tweet_id = status_id
#         contribution.tweet_sent = 1
#         contribution.tweet_dt = datetime.now()
#         contribution.replied_to_status_id = replied_to_status_id        
#         session.add(contribution)
#         session.commit()
#         session.refresh(contribution)  
        
#         # session.close()            
 
# # def update_sent_expenditure_tweet(expenditure_id,status_id, tweet_text):
# #     with Session(engine) as session:
# #         statement = select(Expenditure).where(Expenditure.expenditure_id == expenditure_id)
# #         results = session.exec(statement)
# #         expenditure = results.one()
# #         # print("ExpenditureFiler:", expenditure.filer_name, expenditure.expenditure_amount)
# #         # print(tweet_text)
# #         expenditure.tweet_sent_text = tweet_text
# #         expenditure.tweet_id = status_id
# #         session.add(expenditure)
# #         session.commit()  
  
# def update_sent_expenditure_tweet(expenditure_id,status_id, tweet_text, replied_to_status_id):
#     with Session(engine) as session:
#         statement = select(Expenditure).where(Expenditure.expenditure_id == expenditure_id)
#         results = session.exec(statement)
#         expenditure = results.one()
#         # print("ExpenditureFiler:", expenditure.filer_name, expenditure.expenditure_amount)
#         # print(tweet_text)
#         expenditure.tweet_sent_text = tweet_text
#         expenditure.tweet_id = status_id
#         expenditure.tweet_sent = 1
#         expenditure.tweet_dt = datetime.now()
#         expenditure.replied_to_status_id = replied_to_status_id
#         session.add(expenditure)
#         session.commit() 
#         session.refresh(expenditure)  
    
def select_expenditure_payee_distinct():
    with Session(engine) as session:
        statement = select(Expenditure.payee_or_recipient_or_in_kind_contributor_type, 
                           Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
                           Expenditure.first_name, 
                           Expenditure.middle_name
                        #    Expenditure.address_1,
                        #    Expenditure.address_2,
                        #    Expenditure.city,
                        #    Expenditure.state,
                        #    Expenditure.zip
                           
                           ).distinct()
        results = session.exec(statement)
        rtn_results = results.fetchall() 
    return rtn_results
        
def select_expenditure_payee_name_distinct():
    with Session(engine) as session:
        statement = select(
                        #    Expenditure.payee_or_recipient_or_in_kind_contributor_type, 
                           Expenditure.payee_or_recipient_or_in_kind_contributor_name, 
                           Expenditure.first_name, 
                           Expenditure.middle_name
                        #    Expenditure.address_1,
                        #    Expenditure.address_2,
                        #    Expenditure.city,
                        #    Expenditure.state,
                        #    Expenditure.zip
                           
                           ).distinct()
        results = session.exec(statement)
        rtn_results = results.fetchall() 
    return rtn_results        
def select_contribution_contributor_distinct():
    with Session(engine) as session:
        statement = select(Contribution.contributor_or_transaction_source_type, 
                           Contribution.contributor_or_source_name_individual_last_name, 
                           Contribution.first_name, 
                           Contribution.middle_name,
                           Contribution.address_1,
                           Contribution.address_2,
                           Contribution.city,
                           Contribution.state,
                           Contribution.zip                           
                           ).distinct()
        results = session.exec(statement)
        rtn_results = results.fetchall() 
    return rtn_results   

def insert_error_log(error_message_in):
    with Session(engine) as session:
        error = ErrorLog(
            error_message = error_message_in            
        )
        session.add(error)
        session.commit()
        session.close()
        
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
    # insert_error_log(error_message_in='this is an error message')
    org_id = 7621
    select_contribution_filer(org_id=org_id)
    # select_contributions_by_org(org_id=12345, unsent_only=False, unbuilt_only=True)
    # payee = select_expenditure_payee_distinct()
    # # [build_expendture_payee(x) for x in select_expenditure_payee_distinct]
    # for x in payee:
        # # print(x)
        # # print(x.payee_or_recipient_or_in_kind_contributor_name)
        # payee_type = x.payee_or_recipient_or_in_kind_contributor_type
        # payee_name = x.payee_or_recipient_or_in_kind_contributor_name
        # last_name = x.payee_or_recipient_or_in_kind_contributor_name
        # first_name = x.first_name
        # middle_name = x.middle_name
        # # address_1 = x.address_1
        # # address_2 = x.address_2
        # # city = x.city
        # # state = x.state
        # # zip = x.zip  
        # if payee_type == 'Individual':
        #     if middle_name != None:
        #         payee_name = last_name + ', ' + first_name + ' ' + middle_name
        #         payee = build_expenditure_payee(payee_name_in=payee_name, payee_type_in=payee_type,last_name_in=last_name,first_name_in=first_name,middle_name_in=middle_name
        #                                         # ,address_1_in=address_1,address_2_in=address_2,city_in=city,state_in=state,zip_in=zip
        #                                         )
        #         insert_expenditure_payee(payee_in=payee)
        #     elif middle_name == None:
        #         payee_name = last_name + ', ' + first_name
        #         payee = build_expenditure_payee(payee_name_in=payee_name, payee_type_in=payee_type,last_name_in=last_name,first_name_in=first_name,middle_name_in=''
        #                                         # ,address_1_in=address_1,address_2_in=address_2,city_in=city,state_in=state,zip_in=zip
        #                                         )
        #         insert_expenditure_payee(payee_in=payee)
        # if payee_type != 'Individual':
        #     payee = build_expenditure_payee(payee_name_in=payee_name, payee_type_in=payee_type,last_name_in='',first_name_in='',middle_name_in=''
        #                                     # ,address_1_in=address_1,address_2_in=address_2,city_in=city,state_in=state,zip_in=zip
        #                                     )
        #     insert_expenditure_payee(payee_in=payee)
            


      
                
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