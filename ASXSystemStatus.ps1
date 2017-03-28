$System = 'ASX+Trade','ASX24+(NTP)','Chess','Austraclear','Genium','Calypso+(OTC+Clearing)','ASX+Collateral','DCS','ASX+Online',
'Test+Systems','Supporting+Services+and+Platforms'

$SystemStatus = @()

$System | ForEach-Object {
    $url = 'https://pub.s7.exacttarget.com/0b0bg154xcs?SystemName='+ $_

    $page = Invoke-WebRequest $url 


    $myobj = New-Object psobject -Property @{
        
        System = ($_).replace('+',' ')
        Status = (($page.AllElements | Where-Object {$_.tagname -eq 'LI'}).Class).replace('status','')

    }

    $SystemStatus += $myobj
}

$systemstatus