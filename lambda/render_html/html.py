html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About Me</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background: #f5f7fa;
        }

        .container {
            max-width: 900px;
            margin: 50px auto;
            background: #fff;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }

        .header {
            text-align: center;
        }

        .header h1 {
            margin: 0;
            font-size: 36px;
            color: #333;
        }

        .header p {
            color: #777;
            font-size: 16px;
        }

        .about {
            margin-top: 30px;
            line-height: 1.8;
            color: #444;
        }

        .skills {
            margin-top: 30px;
        }

        .skills h2 {
            margin-bottom: 10px;
        }

        .skill-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .skill {
            background: #007bff;
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 14px;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
        }

        .btn {
            text-decoration: none;
            background: #28a745;
            color: white;
            padding: 12px 25px;
            border-radius: 25px;
            display: inline-block;
            transition: 0.3s;
        }

        .btn:hover {
            background: #218838;
        }
    </style>
</head>
<body>

<div class="container">

    <div class="header">
        <h1>Ruhul Amin</h1>
        <p>Data Engineer | Kafka | Flink | ETL Specialist</p>
    </div>

    <div class="about">
        <h2>About Me</h2>
        <p>
            I am a passionate Data Engineer with experience in building scalable data pipelines 
            using modern technologies like Kafka, Debezium, and Apache Flink. 
            I enjoy solving complex data problems and working with real-time streaming systems.
        </p>
        <p>
            Currently, I am focused on enhancing my skills in distributed systems, 
            cloud technologies, and real-time data processing.
        </p>
    </div>

    <div class="skills">
        <h2>Skills</h2>
        <div class="skill-list">
            <div class="skill">Kafka</div>
            <div class="skill">Flink</div>
            <div class="skill">MySQL</div>
            <div class="skill">Docker</div>
            <div class="skill">Python</div>
            <div class="skill">ETL</div>
        </div>
    </div>

    <div class="footer">
        <a href="#" class="btn">Contact Me</a>
    </div>

</div>

</body>
</html>
    """