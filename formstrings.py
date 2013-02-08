import urllib
# ----------------------------------------------------
# Bits and pieces for the form on the first page
# ----------------------------------------------------	
def SelectChannelButtons():
	s = ("""    
	
			<div class='form-actions'>
				<a href='#' onClick='SelectType(".normal"); return false;' class="btn">Select all channels</a>
				<a href='#' onClick='SelectType(".freeview"); return false;' class="btn">Select Freeview channels</a>
				<a href='#' onClick='SelectType(".sky"); return false;' class="btn">Select Sky channels</a>
				<a href='#' onClick='Unselect(); return false;' class="btn">Remove selections</a>
			</div>

			""")
	
	return s


def GetFreeview(): 
	channels = ['Channel 4 HD', 'BBC1', 'BBC1 HD', 'BBC2', 'BBC3', 'BBC4', 'BBC News', 'BBC HD', 'CBBC', 'CBeebies', 'Channel 4', 
			'More4', 'Film4', 'E4', '4Music', 'Channel 5', 'Channel 5 HD', '5*', '5USA', 'ITV1', 'ITV2', 'ITV3', 'ITV4', 'ITV1 HD', 
			'CITV', 'S4C', 'Quest', 'Yesterday', 'Challenge', 'Pick TV', 'Dave']
	return channels
def GetSky(): 
	channels = ['Sky Atlantic', 'Sky 1', 'Sky Living', 'Sky Arts 1', 'Sky Arts 2', 'Comedy Central', 'FX']
	return channels	