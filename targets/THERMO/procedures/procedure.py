# Script Runner test script
cmd("THERMO EXAMPLE")
wait_check("THERMO STATUS BOOL == 'FALSE'", 5)
