import unittest
from unittest.mock import patch, MagicMock
import main

class TestMainScript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = main.root

    @classmethod
    def tearDownClass(cls):
        cls.app.destroy()

    def test_file_loading(self):
        file_path = "AbbList.xlsx"
        data = main.lade_woerterbuch(file_path)
        self.assertIsInstance(data, dict)
        self.assertTrue(data)  # Check if data is not empty

    @patch('main.abkuerzungen_beschreibungen', {'abc': [('Test Description', 'Test Detailed Description')]})
    def test_search_found(self):
        main.eingabe_abkuerzung_var.set('abc')
        main.suche_beschreibung()
        text_content = main.beschreibungen_text.get(1.0, 'end')
        self.assertIn('Test Description', text_content)

    @patch('main.abkuerzungen_beschreibungen', {'def': [('Test Description', '')]})
    def test_search_not_found(self):
        main.eingabe_abkuerzung_var.set('xyz')
        main.suche_beschreibung()
        text_content = main.beschreibungen_text.get(1.0, 'end')
        self.assertEqual(text_content.strip(), 'Abkürzung nicht gefunden')

    @patch('main.abkuerzungen_beschreibungen', {'abc': [('Test Description', 'Test Detailed Description')]})
    def test_detailed_description_window(self):
        main.eingabe_abkuerzung_var.set('abc')
        with patch.object(main.tk.Toplevel, 'title') as mock_title:
            main.suche_beschreibung()
            mock_title.assert_called_once_with("Detailed Description")
            # Unable to directly test detailed description window contents

    @patch('main.abkuerzungen_beschreibungen', {'abc': [('Test Description', '')]})
    def test_statistic_plot(self):
        main.zeige_statistik_plot()
        # Assuming the plot is created, hence unable to directly test its properties

    def test_autocomplete(self):
        entry = MagicMock()
        entry.get.return_value = 'a'
        lista = ['abc', 'abd', 'xyz']
        main.autocomplete(entry, lista)
        entry.__setitem__.assert_called_once_with('values', ['abc', 'abd'])

if __name__ == '__main__':
    unittest.main()
