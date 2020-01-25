import sqlite3
import datetime
import lxml.etree as etree


db_name = "python_db"


class hospital:
  def __init__(self):
    self.id = 0
    self.name = ""
    self.bed_count = 0


class doctor:
  def __init__(self):
    self.id = 0
    self.name = ""
    self.hospital_id = 0
    self.hospital = hospital()
    self.joining_date = date()
    self.speciality = ""
    self.salary = 0
    self.experience = 0


def create_db():
  conn = sqlite3.connect(db_name)
  res = True

  try:
    with conn:
      conn.execute("CREATE TABLE IF NOT EXISTS `Hospital` ( `Hospital_Id` INT UNSIGNED NOT NULL , `Hospital_Name` TEXT "
                   "NOT "
                   "NULL , `Bed_Count` INT , PRIMARY KEY (`Hospital_Id`))")

      conn.execute("CREATE TABLE IF NOT EXISTS `Doctor` ( `Doctor_Id` INT UNSIGNED NOT NULL , `Doctor_Name` TEXT NOT "
                   "NULL "
                   ", `Hospital_Id` INT NOT NULL , `Joining_Date` DATE NOT NULL , `Speciality` TEXT NULL , `Salary` INT "
                   "NULL , `Experience` INT NULL , PRIMARY KEY (`Doctor_Id`))")

      conn.execute("INSERT INTO `hospital` (`Hospital_Id`, `Hospital_Name`, `Bed_Count`) VALUES ('1', 'Mayo Clinic', "
                   "'200'), ('2', 'Cleveland Clinic', '400'), ('3', 'Johns Hopkins', '1000'), ('4', 'UCLA Medical "
                   "Center', '1500')")

      conn.execute("INSERT INTO `doctor` (`Doctor_Id`, `Doctor_Name`, `Hospital_Id`, `Joining_Date`, `Speciality`, "
                   "`Salary`, `Experience`) VALUES ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), "
                   "('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), ('103', 'Susan', '2', "
                   "'2016-05-19', 'Garnacologist', '25000', NULL), ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', "
                   "'28000', NULL), ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), ('106', "
                   "'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), ('107', 'Richard', '4', "
                   "'2014-08-21', 'Garnacologist', '32000', NULL), ('108', 'Karen', '4', '2011-10-17', 'Radiologist', "
                   "'30000', NULL)")

    rows = cur.fetchall()

  except BaseException as ex:
    res = False
  finally:
    conn.close()

  return res


def print_verion():
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("select sqlite_version();")
    print(cur.fetchone())

  except BaseException as ex:
    print("Error: {}".format(ex))

  finally:
    conn.close()


def read_doctors():
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
      "SELECT `Doctor_Id`, `Doctor_Name`, `Hospital_Id`, `Joining_Date`, `Speciality`, `Salary`, `Experience` FROM "
      "`doctor`")

    rows = cur.fetchall()

    doctors_res = []

    for r in rows:
      doctor.id = r[0]
      doctor.name = r[1]
      doctor.hospital_id = r[2]
      doctor.joining_date = r[3]
      doctor.speciality = r[4]
      doctor.salary = r[5]
      doctor.experience = r[6]

      doctors_res.append(doctor)

  except BaseException as ex:
    print("read_doctors Error: {}".format(ex))

  return doctors_res


def read_doctor_by_id(doctor_id):
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
      "SELECT `Doctor_Id`, `Doctor_Name`, `Hospital_Id`, `Joining_Date`, `Speciality`, `Salary`, `Experience` FROM "
      "`doctor` WHERE Doctor_Id=:doctor_id", {"doctor_id": doctor_id})

    r = cur.fetchone()

    if r is not None:
      doctor.id = r[0]
      doctor.name = r[1]
      doctor.hospital_id = r[2]
      doctor.joining_date = r[3]
      doctor.speciality = r[4]
      doctor.salary = r[5]
      doctor.experience = r[6]

  except BaseException as ex:
    print("read_doctor_by_id Error: {}".format(ex))

  return doctor


def read_doctors_by_speciality(speciality):
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
      "SELECT `Doctor_Id`, `Doctor_Name`, `Hospital_Id`, `Joining_Date`, `Speciality`, `Salary`, `Experience` FROM "
      "`doctor` WHERE Speciality=:speciality", {"speciality": speciality})

    rows = cur.fetchall()

    doctors_res = []

    for r in rows:
      doctor.id = r[0]
      doctor.name = r[1]
      doctor.hospital_id = r[2]
      doctor.joining_date = r[3]
      doctor.speciality = r[4]
      doctor.salary = r[5]
      doctor.experience = r[6]

      doctors_res.append(doctor)

  except BaseException as ex:
    print("read_doctors_by_speciality Error: {}".format(ex))


def read_doctors_by_hospital_name(hospital_name):
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
      "SELECT `Doctor_Id`, `Doctor_Name`, `doctor`.`Hospital_Id`, `Joining_Date`, `Speciality`, `Salary`, "
      "`Experience`, 'hospital'.`Hospital_Name`, 'hospital'.`Bed_Count` FROM "
      "`doctor` INNER JOIN 'hospital' ON doctor.Hospital_Id=hospital.Hospital_Id WHERE "
      "hospital.Hospital_Name=:hospital_name", {"hospital_name": hospital_name})

    rows = cur.fetchall()

    doctors_res = []

    for r in rows:
      doctor.id = r[0]
      doctor.name = r[1]
      doctor.hospital_id = r[2]

      doctor.hospital = hospital()
      doctor.hospital.id = r[2]
      doctor.hospital.name = r[7]
      doctor.hospital.bed_count = r[8]

      doctor.joining_date = r[3]
      doctor.speciality = r[4]
      doctor.salary = r[5]
      doctor.experience = r[6]

      doctors_res.append(doctor)

  except BaseException as ex:
    print("read_doctors_by_hospital_name Error: {}".format(ex))


def read_hospitals():
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT `Hospital_Id`, `Hospital_Name`, `Bed_Count` FROM `hospital`")

    rows = cur.fetchall()

    hospitals_res = []

    for r in rows:
      hospital.id = r[0]
      hospital.name = r[1]
      hospital.bed_count = r[2]

      hospitals_res.append(hospital)

  except BaseException as ex:
    print("read_hospitals Error: {}".format(ex))

  return hospitals_res


def read_hospital_by_id(hospital_id):
  try:
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT `Hospital_Id`, `Hospital_Name`, `Bed_Count` FROM `hospital` WHERE Hospital_Id=:hospital_id",
                {"hospital_id": hospital_id})

    r = cur.fetchone()

    if r is not None:
      hospital.id = r[0]
      hospital.name = r[1]
      hospital.bed_count = r[2]

  except BaseException as ex:
    print("read_hospital_by_id Error: {}".format(ex))

  return hospital


def update_doctor_experience(doctor_id, experience):
  try:
    conn = sqlite3.connect(db_name)
    with conn:
      conn.execute(
        "UPDATE `doctor` SET Experience=:experience WHERE Doctor_Id=:doctor_id",
        {"doctor_id": doctor_id, "experience": experience})
  except BaseException as ex:
    print("update_doctor_experience Error: {}".format(ex))


def doctors_to_xml(doctors, file_path):
  root_node = etree.Element("Envelope", attrib={"xmlns": "http://schemas.xmlsoap.org/soap/envelope/"})
  body_node = etree.SubElement(root_node, "Body")
  doctors_node = etree.SubElement(body_node, "Doctors")
  for d in doctors:
    doctor_node = etree.SubElement(doctors_node, "Doctor")
    doctor_id_node = etree.SubElement(doctor_node, "Doctor_ID")
    doctor_id_node.text = str(d.id)
    personal_data_node = etree.SubElement(doctor_node, "Personal_Data")
    doctor_name_node = etree.SubElement(personal_data_node, "Name")
    doctor_name_node.text = d.name
    doctor_speciality_node = etree.SubElement(personal_data_node, "Speciality")
    doctor_speciality_node.text = d.speciality
    doctor_salary_node = etree.SubElement(personal_data_node, "Salary")
    doctor_salary_node.text = str(d.salary)

  # print(etree.tostring(root_node))

  try:
    with open(file_path, 'wb') as f:
      tree = etree.ElementTree(root_node)
      tree.write(f, pretty_print=True)
  except BaseException as ex:
    print("doctors_to_xml error: {}".format(ex))
    return False
  except:
    print("doctors_to_xml unknown error: {}".format(sys.exc_info()[1]))
    return False

  return True


def main():
  create_db()
  print_verion()
  read_doctors()
  read_hospitals()

  read_doctor_by_id(101)
  read_hospital_by_id(2)

  read_doctors_by_speciality("Pediatric")
  read_doctors_by_hospital_name("Cleveland Clinic")

  update_doctor_experience(101, 4567)
  read_doctor_by_id(101)

  all_doctors = read_doctors()
  doctors_to_xml(all_doctors, "doctors.xml")


if __name__ == "__main__":
  main()
