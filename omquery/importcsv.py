from .models import NimsTmus
import csv
import os
import gzip


data_dir=r'C:\ProgramData\bin\pyworkspace\sankar228-git\medgraphql\omquery\data'

def loadcsvdata():
    delimiter = '|'
    has_header = True
    for file in os.listdir(data_dir):
        if (file.endswith(".gz")):
            print("file: {}".format(file))
            with gzip.open(os.path.join(data_dir, file), 'rt') as gfile:
                csv_reader = csv.reader(gfile, delimiter=delimiter)
                line_count = 0
                    
                for row in csv_reader:
                    if has_header and line_count == 0:
                        print("This is the header {}".format(row))
                        line_count += 1
                        continue
                    else:
                        line_count += 1
                        print("Record {}".format(row))
                        nims_record = NimsTmus(region=row[0],oss_market=row[1],vendor=row[2],
                                            technology=row[3],site_name=row[4],gnodeb_id=row[5]
                                            ,cellname=row[6],gnodeb_name=row[7],cell_id=row[8],
                                            address=row[9],city=row[10],state=row[11],zip=row[12],
                                            coveragetype=row[13],RF_Solution=row[14],latitude_sector=row[15],
                                            longitude_sector=row[16],azimuth=row[17],horizontal_bw=row[18],
                                            vertical_bw=row[19],antenna_height_ft=row[20],antenna_gain=row[21],
                                            antenna_model=row[22],propagation_model=row[23],rs_power=row[24],
                                            pa_power=row[25],electrical_tilt=row[26],mcc=row[27],mnc=row[28],
                                            lac=row[29],sectorname=row[30],tac=row[31],pci=row[32],
                                            carrier_nm=row[33],oss=row[34],cell_status=row[35],
                                            on_airdate=row[36],ul_ch_bw=row[37],dl_ch_bw=row[38],
                                            earfcn_dl=row[39],earfcn_ul=row[40],NED_export_date=row[41],
                                            gnodeb_status=row[42],Site_Type=row[43],TimeZone=row[44],
                                            Cell_Type=row[45],sector_id=row[46],Carrier_id=row[47],
                                            cgi=row[48],Band=row[49],antenna_agl_ft=row[50],total_loss=row[51]
                                            ,mechanical_tilt=row[52],Cell_Radius=row[53])
                        try:
                            nims_record.save()
                        except:
                            print("bad record rec#{} , rec:".format(line_count, row))
 
if __name__ == "__main__":
    loadcsvdata()        