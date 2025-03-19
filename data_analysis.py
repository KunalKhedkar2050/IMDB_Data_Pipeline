from pyspark.sql import SparkSession

def analyze_data():
    spark = SparkSession.builder.appName("IMDbAnalysis").getOrCreate()
    df = spark.read.format("delta").load(f"s3://{AWS_S3_PROCESSED_BUCKET}/imdb_processed.delta")
    
    df.createOrReplaceTempView("movies")
    
    # Top 10 highest-rated movies
    top_movies = spark.sql("""
        SELECT primaryTitle, startYear, genres
        FROM movies
        ORDER BY startYear DESC
        LIMIT 10
    """)
    top_movies.show()
    
    # Most popular genres over time
    genre_trends = spark.sql("""
        SELECT genres, count(*) as count
        FROM movies
        GROUP BY genres
        ORDER BY count DESC
        LIMIT 10
    """)
    genre_trends.show()
    
    # Average movie rating per decade
    decade_ratings = spark.sql("""
        SELECT Decade, avg(averageRating) as Avg_Rating
        FROM movies
        GROUP BY Decade
        ORDER BY Decade
    """)
    decade_ratings.show()
    
    # Directors with the most blockbuster movies
    directors_top = spark.sql("""
        SELECT directorName, count(*) as Total_Movies
        FROM movies
        WHERE averageRating >= 8.0
        GROUP BY directorName
        ORDER BY Total_Movies DESC
        LIMIT 10
    """)
    directors_top.show()
    
  