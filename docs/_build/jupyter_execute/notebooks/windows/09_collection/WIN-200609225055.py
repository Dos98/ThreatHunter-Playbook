# Processes Accessing the Microphone Device

## Metadata


|               |    |
|:--------------|:---|
| id            | WIN-200609225055 |
| author        | Roberto Rodriguez @Cyb3rWard0g |
| creation date | 2020/06/09 |
| platform      | Windows |
| playbook link |  |
        

## Technical Description
An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.
Based on some research from [@svch0st](https://twitter.com/svch0st) you can to determine when and how long a process had access to the microphone of an endpoint by monitoring the following registry key:
  * HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone\.

## Hypothesis
Adversaries might be accessing the microphone in endpoints over the network.

## Analytics

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/collection/msf_record_mic.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Analytic I


| FP Rate  | Log Channel | Description   |
| :--------| :-----------| :-------------|
| Low       | ['Security']          | Look for non-system accounts getting a handle and access lsass            |
            

df = spark.sql(
    '''
SELECT *
FROM mordorTable
WHERE Channel = "Security"
    '''
)
df.show(10,False)

## Detection Blindspots


## Hunter Notes


## Hunt Output


## References
* https://medium.com/@7a616368/can-you-track-processes-accessing-the-camera-and-microphone-7e6885b37072