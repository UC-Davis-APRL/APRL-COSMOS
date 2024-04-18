# Script Runner test script
cmd("LCELL EXAMPLE")
wait_check("LCELL STATUS BOOL == 'FALSE'", 5)
