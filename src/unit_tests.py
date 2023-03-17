import unittest
from rna_transcription import dna_transcription
from statistical_moments import statistical_moments

class TestDNATranscription(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(dna_transcription('GGCTA'), 'CCGAU')
        self.assertEqual(dna_transcription('ACTGATA'), 'UGACUAU')
        self.assertEqual(dna_transcription(''), '')
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            dna_transcription(123)
        with self.assertRaises(KeyError):
            dna_transcription('AUCGT')
        with self.assertRaises(KeyError):
            dna_transcription('\\')


class TestStatisticalMoments(unittest.TestCase):
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            statistical_moments([], k=1, central=False)

    def test_moments(self):
        self.assertEqual(statistical_moments([1, 2, 3], k=1, central=False), 2)
        self.assertEqual(statistical_moments([1, 2, 3, 4], k=2, central=False), 7.5)

    def test_central_moments(self):
        self.assertEqual(statistical_moments([1, 2, 3, 4], k=1, central=True), 0)
        self.assertEqual(statistical_moments([1, 2, 3, 4], k=2, central=True), 1.25)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
