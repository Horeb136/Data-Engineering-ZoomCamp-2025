# How did I really install Spark and PySpark on my Linux?

This guide documents the exact steps taken to successfully install **Java**, **Apache Spark**, and **PySpark** on a **Linux (Ubuntu/Debian/WSL)** system.

---

## **1️⃣ Install Java (JDK 11)**
Spark requires **Java 8 or 11**. The recommended version is **OpenJDK 11**.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openjdk-11-jdk -y
```

✅ **Verify the installation**:
```bash
java -version
```
Expected output:
```
openjdk version "11.0.XX"  (varies)
OpenJDK Runtime Environment (build 11.0.XX)
OpenJDK 64-Bit Server VM (build 11.0.XX)
```

---

## **2️⃣ Install Apache Spark**
### **🔹 Download and Extract Spark**
```bash
wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
tar -xzf spark-3.3.2-bin-hadoop3.tgz
mv spark-3.3.2-bin-hadoop3 ~/spark
rm spark-3.3.2-bin-hadoop3.tgz
```

### **🔹 Set Environment Variables**
Edit your **`~/.bashrc`**:
```bash
nano ~/.bashrc
```
Add the following lines at the end:
```bash
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"

export SPARK_HOME="$HOME/spark"
export PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"

export PYSPARK_PYTHON=python3
```
Save and exit (`Ctrl + X`, then `Y`, then `Enter`).

Apply changes:
```bash
source ~/.bashrc
```

✅ **Verify Spark installation**:
```bash
spark-shell
```
Expected output:
```
Spark context Web UI available at http://your-hostname:4040
Spark session available as 'spark'.
```
To exit Spark shell:
```scala
:quit
```

---

## **3️⃣ Install and Configure PySpark**
### **🔹 Check Python Version**
```bash
python3 --version
```
If Python is not installed:
```bash
sudo apt install python3 -y
```

### **🔹 Locate `py4j` Version**
```bash
ls $SPARK_HOME/python/lib/ | grep py4j
```
Example output:
```
py4j-0.10.9.5-src.zip
```

### **🔹 Update `PYTHONPATH`**
Edit **`~/.bashrc`**:
```bash
nano ~/.bashrc
```
Add:
```bash
export PYTHONPATH="$SPARK_HOME/python:$PYTHONPATH"
export PYTHONPATH="$SPARK_HOME/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"
```
(If `py4j-0.10.9.5-src.zip` is a different version, update accordingly.)

Apply the changes:
```bash
source ~/.bashrc
```

✅ **Verify PySpark installation**:
```bash
pyspark
```
Expected output:
```
SparkSession available as 'spark'.
```

To exit PySpark:
```python
exit()
```

---

🚀 **Now, Apache Spark and PySpark are fully installed on your Linux system!** 🚀
