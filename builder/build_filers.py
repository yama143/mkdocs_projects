from dal_classes import SelectFiler



def main() -> None:
    filers = SelectFiler().all()
    hdr_columns = "| filer name | expenditure amount { data-sort-method='number' } | receipt amount { data-sort-method='number' } |"
    hdr_break =   '| :--------------------------------- | :--------------------------------- | :--------------------------------- |'
    hdr = hdr_columns + '\n' + hdr_break + '\n'
    print(hdr)
    f = open("filer_table.md", 'w')
    f.write(hdr)
    for filer in filers:
        filer_name = filer.filer_name 
        # exp_cnt = str(filer.expenditure_count)
        exp_amt = str(filer.expenditure_total_amount)
        # rcp_cnt = str(filer.receipt_count) 
        rcp_amt = str(filer.receipt_total_amount)
        
        row = '| '  
        row += filer_name + ' | '
        # row += exp_cnt + ' | '
        row += exp_amt + ' | ' 
        # row += rcp_cnt + ' | '
        row += rcp_amt + ' |'
        row += '\n'
        print(row) 
        f.write(row)
        


      
if __name__ == "__main__":
    main()
    



# ### sortable?
# | Method      | Description                          |
# | ----------- | ------------------------------------ |
# | `GET`       | :material-check:     Fetch resource  |
# | `PUT`       | :material-check-all: Update resource |
# | `DELETE`    | :material-close:     Delete resource |