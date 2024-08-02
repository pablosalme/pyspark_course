# Spark Udemy Course Repository

This repository contains the code and datasets used in the Udemy course on Apache Spark. The course covers various aspects of Spark, including basics, RDD interface, Spark SQL, advanced examples, machine learning with Spark MLlib, and Spark Streaming. Below is the structure of the repository along with descriptions of the sections.

## Repository Structure

```plaintext
├── ml-100k/
│   ├── README
│   ├── allbut.pl
│   ├── mku.sh
│   ├── u.data
│   ├── u.genre
│   ├── u.info
│   ├── u.item
│   ├── u.occupation
│   ├── u.user
│   ├── u1.base
│   ├── u1.test
│   ├── u2.base
│   ├── u2.test
│   ├── u3.base
│   ├── u3.test
│   ├── u4.base
│   ├── u4.test
│   ├── u5.base
│   ├── u5.test
│   ├── ua.base
│   ├── ua.test
│   ├── ub.base
│   ├── ub.test
├── section1_getting_started_with_spark/
│   └── ratings-counter.py
├── section2_spark_basics_and_the_rdd_interface/
│   ├── 1800.csv
│   ├── Book
│   ├── customer-orders.csv
│   ├── fakefriends.csv
│   ├── friends-by-age.py
│   ├── max-temperatures.py
│   ├── min-temperatures.py
│   ├── total_amount.py
│   ├── total_amount_sorted.py
│   ├── word-count-better-sorted.py
│   ├── word-count-better.py
│   └── word-count.py
├── section3_sparkSQL_dataframes_datasets/
│   ├── 1800.csv
│   ├── book.txt
│   ├── customer-orders.csv
│   ├── fakefriends-header.csv
│   ├── fakefriends.csv
│   ├── min-temperatures-dataframe.py
│   ├── spark-sql-dataframe-exercise.py
│   ├── spark-sql-dataframe.py
│   ├── spark-sql.py
│   ├── total_spent_customer.py
│   └── word-count-better-sorted-dataframe.py
├── section4_advanced_examples_spark_programs/
│   ├── degrees-of-separation.py
│   ├── most-obscure-superhero.py
│   ├── most-popular-superhero-dataframe.py
│   ├── movie-similarities-dataframe.py
│   ├── popular-movies-dataframe.py
│   └── popular-movies-nice-dataframe.py
├── section6_machine_learning_sparkml/
│   ├── movie-recommendations-als-dataframe.py
│   ├── real-estate.py
│   ├── realestate.csv
│   ├── regression.txt
│   └── spark-linear-regression.py
└── section7_sparkStreaming_structuredStreaming_GraphX/
    ├── structured-streaming.py
    ├── top-urls.py
    └── logs/
        ├── access_log copy 2.txt
        ├── access_log copy.txt
        └── access_log.txt
```

## Sections Overview

### Section 1: Getting Started with Spark

- `ratings-counter.py`: Introduction to basic Spark operations and the SparkContext.

### Section 2: Spark Basics and the RDD Interface

- Contains scripts and datasets for learning the basics of Spark RDD operations, transformations, and actions.

### Section 3: Spark SQL, DataFrames, and Datasets

- Scripts and data to practice using Spark SQL and DataFrames for data manipulation and querying.

### Section 4: Advanced Examples of Spark Programs

- Advanced Spark programs demonstrating complex transformations and actions on large datasets.

### Section 6: Machine Learning with Spark MLlib

- Machine learning examples using Spark MLlib, including linear regression and ALS for recommendations.

### Section 7: Spark Streaming, Structured Streaming, and GraphX

- Examples of streaming data processing with Spark Streaming and structured streaming, as well as graph processing with GraphX.

## Datasets

The `ml-100k/` directory contains datasets used in various sections of the course. These include movie ratings data and other relevant datasets for performing Spark operations.

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the desired section and run the Python scripts using Spark.
3. Ensure you have the necessary Spark environment set up and the datasets in the correct locations.

## Requirements

- Apache Spark
- Python 3.x
- Any additional libraries mentioned in individual scripts

## Acknowledgements

This repository is based on the Udemy course on Apache Spark. All credit goes to the course instructor for the original content and datasets.

---

Feel free to explore the code and datasets, and use them to enhance your understanding of Apache Spark!
