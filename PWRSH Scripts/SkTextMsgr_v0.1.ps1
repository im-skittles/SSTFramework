echo "------------------------------------------"
echo "-----Skittle_'s Powershell Messenger------"
echo "--------------Version 0.1-----------------"
echo ""
$Recieve = Read-Host -Prompt "Input student ID"
$Message = Read-Host -Prompt "Input Message"
MSG $Recieve $Message
echo ""
echo "------------------Done!-------------------"