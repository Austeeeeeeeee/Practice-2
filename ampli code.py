
with allure.step('Walking to Palettes submenu'):
	err = walker.find_item_path('/mmenu/palette')
	validate_error_ok(err,'Failed to walk to Palettes submenu.')
	Log.debug('Failed to walk to Palettes submenu')

with allure.step('Selecting Palettes submenu'):
	err = walker.press_enter_button(short_press=True)
	validate_error_ok(err, 'Failed to enter Palettes submenu')
	Log.debug('Failed to short-press button') #what message is better? this one or failed to switch palette on?

	'''
	Steps walking to the palettes submenu

with allure.step('Walking to Palettes submenu'):
err = walker.find_item_path('/mmenu/palette')
validate_error_ok(err,'Failed to walk to Palettes submenu.')
Log.debug('Failed to walk to Palettes submenu')

with allure.step('Selecting Palettes submenu'):
err = walker.press_enter_button(short_press=True)
validate_error_ok(err, 'Failed to enter Palettes submenu')
Log.debug('Failed to short-press button') #what message is better? this one or failed to switch palette on?






	for palette in cycle_palettes_list:
		err = walker.press_enter_button(short_press=True)
		validate_error_ok(err,'Failed to switch off {palette}')
		Log.debug('Failed to short-press button')

		err = walker.emulate_encoder(direction=0) #assumming 0 is going forward
		validate_error_ok(err,'Failed to move encoder')
		Log.debug('Failed to moved encoder')

	with allure.step('Exiting the Palettes submenu'):
		err = walker.press_enter_button(short_press=False)
		validate_error_ok(err,'Failed to exit the submenu')

	with allure.step('Exiting the Main Menu'):
		err = walker.press_enter_button(short_press=False)
		validate_error_ok(err,'Failed to exit the Main Menu')

	with allure.step("Get device's state"):
		current_state = _get_state(dut.client)
		assert current_state == default_state,'Device is not in idle state!'
	'''
