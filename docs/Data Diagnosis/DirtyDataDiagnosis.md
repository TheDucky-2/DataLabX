# **Dirty Data Diagnosis**

Imagine opening your fridge and noticing a few problems such as:

- Expired food

- Containers with no labels

- The same item is stored in multiple sections

- Ice spread all over the freezer

- Some ingredients are spilled or mixed with each other.

**Dirty data diagnosis** means the same thing for our data.

It means carefully checking our data to find problems like:

- Numbers written as words or mixed with symbols and text, instead of just numbers.

- Empty data or replaced with words like 'missing' or 'unknown' or symbols like '?'.

- Numbers including units like 'cm' or '$' when they should not.

- Numbers written in scientific notation

> Dirty Data Diagnosis is required because we can’t clean or fix data unless we know exactly what’s wrong with it.

Once, we identify the problems that exist in our data, it would be easier to know what and how to clean it.

##  Dirty Data Diagnosis Overview:

**DirtyDataDiagnosis** in DataLab refers to the check-up of dirt or issues present in numbers, text or date-time data.

It helps us detect:

- Issues with Numerical data (like units, commas, text, symbols, scientific notations present in numbers).
- Issues with Text data (like numbers, symbols, spaces present in text).
- Issues with Datetime data (like symbols, incorrect dates)

### **DataLab Usage:**

We can explore dirty data by importing ``DirtyDataDiagnosis`` class from DataLab.

    from datalab import DirtyDataDiagnosis

    diagnosis = DirtyDataDiagnosis(df)

## Numerical Dirty Data Diagnosis

DataLab allows us to diagnose problems with Numerical Data (numbers), in order to help us decide what cleaning steps may be required.

### Why is this useful?

It helps us identify these in our Numerical Data:

| Diagnosis Type | Description | Diagnosis Method |
|------|-------------|--------|
| Valid numbers | Only valid numbers like ``234`` or ``23.34`` | is_valid |
| Dirty numbers | Numbers that are dirty and require cleaning | is_dirty |
| Text | Only text exists, like ``five`` or ``unknown`` | is_text |
| Symbols | Only symbols exist, like ``?`` or ``--``. | is_symbol |
| Scientific notation | Numbers in scientific notation like ``1.82e+05`` | is_scientific_notation |
| Missing values | Only **pandas built-in missing** values like `None` or `NaN`, etc. | is_missing |
| Units | Numbers containing units like ``cm``, ``kg``, or ``C`` | has_units |
| Symbols in numbers | Numbers containing symbols like ``5,927#`` | has_symbols |
| Commas in numbers | Numbers containing commas like ``30,770`` | has_commas |
| Currency symbols | Numbers containing currency symbols like ``$`` or ``€``| has_currency |
| Single decimals | Numbers containing single decimal like ``1.234`` | has_decimals |
| Double decimals | Numbers containing multiple decimals like ``149.918.17`` | has_double_decimals |
| Leading/trailing spaces | Numbers containing spaces at the beginning or end | has_spaces |

### **DataLab Usage**:

We can diagnose numbers by using ``diagnose_numbers()`` method from the **DirtyDataDiagnosis** class of DataLab.

This method returns a dictionary of DataFrames that follows the following structure:

    diagnosis[column_name][method]

Here, **column_name** refers to the name of the column being diagnosed, and **method** refers to the specific diagnostic method applied.

We can also pass **show_available_methods = True** to see a list of all these options available for diagnosis.

    Available diagnostic methods: ['is_valid', 'is_text', 'is_symbol', 'is_dirty', 'is_missing'] <- A list like this, just longer.

Example:

    num_diagnosis = diagnosis.diagnose_numbers(show_available_methods=True) 

    num_diagnosis['Age']['is_dirty']

Output:  

| Age      | Salary              | Expenses           | Height_cm    | Weight_kg | Temperature_C | Purchase_Amount | Score           | Rating                    | Debt        |
|----------|-------------------|------------------|-------------|-----------|---------------|----------------|----------------|---------------------------|------------|
| five     | 1.04e+05          | 4735.244618878169 | 1,55e+02    | None      | unknown       | None           | 30.70          | 4.888018131992931         | 64,972     |
| missing  | None               | 894429            | 196.34 cm   | ?         | -1.57e+01     | None           | ?              | 4.31                      | 27,400cm   |
| 28$      | 112877.67251785153 | 1040.45          | 171.40 cm   | 49,12     | -6            | 4344.39        | 2.24           | 4.14                      | 67682      |
| 1,62e+00 | None               | ?                 | 188.38      | 13W       | -17.10        | 4939.82        | 1,37e+01       | approx 1000               | 49,979,88  |
| ?        | 114,154kg          | 3886.04358926301 | None        | 67cm      | 4.19e+01      | None           | ?              | four                      | None       |
<br>

We can see:

- An extremely dirty and hostile Numerical data
- Columns 'Age' showing all kinds of dirt in those 5 rows
- Other columns also having dirty data



    








