BEGIN{
    print "                                   INVENTORY REPORT" ;
    print "------------------------------------------------------------------------------------------" ;
    print "| Part Number | Price  | Quantity on Hand | Reorder Point | Minimum Order | Order Amount |" ;
    print "|-------------|--------|------------------|---------------|---------------|--------------|" ;
}  
{
    value_of_part_number = $1 ; 
    value_of_price = $2 ;
    value_of_quantity_on_hand = $3 ;
    value_of_reorder_point = $4 ;
    value_of_minimum_order = $5 ;
    if(value_of_quantity_on_hand<value_of_reorder_point)
      value_of_order_amount = $4+$5-$3 ;
    else
      value_of_order_amount = 0 ;
    printf("|     %s",value_of_part_number) ;
    printf("    | %5.2f",value_of_price) ;
    printf("  |        %2d",value_of_quantity_on_hand) ;
    printf("        |      %d",value_of_reorder_point) ;
    printf("       |      %2d ",value_of_minimum_order) ;
    printf("      |     %2d       |\n",value_of_order_amount) ;
}
END{    
    print "------------------------------------------------------------------------------------------" ;
    print "                                     END REPORT" ;
}