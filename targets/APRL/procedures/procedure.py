# Script Runner test script
cmd("APRL EXAMPLE")
wait_check("APRL STATUS BOOL == 'FALSE'", 5)
