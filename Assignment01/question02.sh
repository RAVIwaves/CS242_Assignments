#! /bin/bash

echo "                      PAYROLL REGISTER"
echo "|===========================================================|"

#Lopp runs through each line of EMPLOYEE.txt
while IFS=" " read -r data1 data2 data3 data4 data5 ;
do
    employee_no=$data1
    department_no=$data2
    pay_rate=$data3
    exempt=$data4
    hours_worked=$data5
    if [ $exempt == "Y" ]
    then
        #for the case when exempt = Y
        overtime_pay=0
        base_pay=$(echo $pay_rate $hours_worked | awk '{printf("%.2f",$1*$2);}')
        total_pay=$(echo $base_pay $overtime_pay | awk '{printf("%.2f",$1+$2)}')

        #Printing Output
        echo "| Employee No:    Pay rate:    Hours worked:    Department: |"
        echo "| $employee_no            $pay_rate         $hours_worked               $department_no          |"
        echo "| Exempt:         Base pay:    Overtime pay:    Total pay:  |"
        echo "| $exempt               $base_pay       $overtime_pay                $total_pay      |"
        echo "|===========================================================|"
    else
        if (( $hours_worked > 40 ))
        then
            #for the case when exempt = N and hours worked > 40
            base_pay=$(echo $pay_rate | awk '{printf("%.2f",$1*40)}')
            extra_time=$(echo $hours_worked | awk '{printf("%d",$1-40)}')
            over_time_pay_rate=$(echo $pay_rate | awk '{printf("%f",$1*1.5)}')
            overtime_pay=$(echo $over_time_pay_rate $extra_time | awk '{printf("%5.2f",$1*$2)}')
            total_pay=$(echo $base_pay $overtime_pay | awk '{printf("%.2f",$1+$2)}')

            #Printing Output
            echo "| Employee No:    Pay rate:    Hours worked:    Department: |"
            echo "| $employee_no            $pay_rate         $hours_worked               $department_no          |"
            echo "| Exempt:         Base pay:    Overtime pay:    Total pay:  |"
            echo "| $exempt               $base_pay       $overtime_pay            $total_pay      |"
            echo "|===========================================================|"
        else
            #for the case when exemp = N and hours worked <= 40
            overtime_pay=0
            base_pay=$(echo $pay_rate $hours_worked | awk '{printf("%.2f",$1*$2);}')
            total_pay=$(echo $base_pay $overtime_pay | awk '{printf("%.2f",$1+$2)}')

            #Printing Output
            echo "| Employee No:    Pay rate:    Hours worked:    Department: |"
            echo "| $employee_no            $pay_rate         $hours_worked               $department_no          |"
            echo "| Exempt:         Base pay:    Overtime pay:    Total pay:  |"
            echo "| $exempt               $base_pay       $overtime_pay                $total_pay      |"
            echo "|===========================================================|"
        fi
    fi
done < EMPLOYEE.txt #inserting input file
echo "                           END"

