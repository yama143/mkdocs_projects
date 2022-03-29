from dal_classes import SelectOrgContributions



def main() -> None:
    receipts = SelectOrgContributions(org_id=7688).all()    
    hdr_columns = "| payor name | reciept amt { data-sort-method='number' } | receipt date { data-sort-method='date' } |"
    hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- |'
    hdr = hdr_columns + '\n' + hdr_break + '\n'
    print(hdr)
    f = open("receipt_table.md", 'w')
    f.write(hdr)
    for rcp in receipts:

        payor_name = rcp.payor_name 
        rcp_amt = str(rcp.receipt_date)

        rcp_date = str(rcp.receipt_amount)
        
        row = '| '  
        row += payor_name + ' | '
        row += rcp_amt + ' | ' 

        row += rcp_date + ' |'
        row += '\n'
        print(row) 
        f.write(row)
        


      
if __name__ == "__main__":
    main()
    