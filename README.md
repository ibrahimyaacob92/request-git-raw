# request-git-raw
To pull raw file from repository and save it to a local machine, or just read them

```python
import GitFileRequestor

file = GitFileRequestor('my_username','my_password')
x = file.get_raw_file('ibrahimyaacob92','excel_vba_essential','cohort-analysis-sample.xlsx', "E:\myDesktop\mystuff")
```
code above will get the raw **cohort-analysis-sample.xlsx** file from **ibrahimyaacob92/excel_vba_essential** and save it into your local machine **E:\myDesktop\mystuff**
