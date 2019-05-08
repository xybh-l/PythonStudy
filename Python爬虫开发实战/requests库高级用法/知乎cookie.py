import requests

headers = {
'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
	'Host':'www.zhihu.com',
	'cookie':'tgw_l7_route=7c109f36fa4ce25acb5a9cf43b0b6415; _zap=7725ecd7-e3cb-494e-855d-d6927ad58db7; _xsrf=fI9QC6cih0iJ5oAP223KTc9OeTILnEMS; d_c0="AHDnQ9VSZA-PTinWG6knqE06q4_8CBBatZI=|1557210638"; capsion_ticket="2|1:0|10:1557210661|14:capsion_ticket|44:MTkzYjljMzI4ZDY4NDgwMTk5YTg2MDFmMGY3MjQxMDk=|76a9a11aafd9d1170b02faad2f46708d6bfb2611a5797835c8bbbb32bbb272fc"; z_c0="2|1:0|10:1557210678|4:z_c0|92:Mi4xT0lGVUF3QUFBQUFBY09kRDFWSmtEeVlBQUFCZ0FsVk5OblMtWFFBOHdpQUtiM09tMVdPbEVYcHkxb0tvZGd5LWhB|c26829b7a288fc83fe31443c873db1101a69e1ffa4b4ed9d7fe2a1b08f75b0bc"; unlock_ticket="AEAAm1oWWAomAAAAYAJVTT4t0VzQLQxxaE8VxcxMBDhDwhHG5pGMkQ=="'
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
