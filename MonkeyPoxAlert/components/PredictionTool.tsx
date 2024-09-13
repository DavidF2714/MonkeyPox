"use client";
import React, { useState } from 'react';
import Divider from '@mui/material/Divider';
import Stack from '@mui/material/Stack';
import { Snackbar } from '@mui/material';
import MuiAlert, { AlertProps, AlertColor } from '@mui/material/Alert';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

// Explicitly specify the ref type as HTMLDivElement
const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const PredictionTool = () => {
  const [formData, setFormData] = useState({
    systemicIllness: '', // 'lymphaden', 'Fever', 'myalgia', 'None'
    rectalPain: '',
    soreThroat: '',
    penileOedema: '',
    oralLesions: '',
    solitaryLesion: '',
    swollenTonsils: '',
    hivInfection: '',
    sti: ''
  });

  const [openSnackbar, setOpenSnackbar] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [snackbarSeverity, setSnackbarSeverity] = React.useState<AlertColor | undefined>(undefined);


  // Handle change in radio buttons
  const handleChange = (event:React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value
    }));
  };


  const handleSubmit = async (event:React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    // Generate the features array
    const features = [
      1, // Index 0: Always 1
      formData.rectalPain === 'yes' ? 1 : 0,
      formData.soreThroat === 'yes' ? 1 : 0,
      formData.penileOedema === 'yes' ? 1 : 0,
      formData.oralLesions === 'yes' ? 1 : 0,
      formData.solitaryLesion === 'yes' ? 1 : 0,
      formData.swollenTonsils === 'yes' ? 1 : 0,
      formData.hivInfection === 'yes' ? 1 : 0,
      formData.sti === 'yes' ? 1 : 0,
      formData.systemicIllness === 'None' ? 1 : 0,
      formData.systemicIllness === 'Fever' ? 1 : 0,
      formData.systemicIllness === 'lymphaden' ? 1 : 0,
      formData.systemicIllness === 'myalgia' ? 1 : 0
    ];

    const requestBody = {
      features: JSON.stringify(features)
    };

    console.log("Request body: ", requestBody.features);

    try {
      const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      if (response.ok) {
        const result = await response.json();
        console.log('Success:', result);

        if (result.prediction === 1) {
          setSnackbarMessage('Existe la probabilidad de que estés contagiado de viruela de mono. Te recomendamos que consultes a un médico.');
          setSnackbarSeverity('warning');
        } else {
          setSnackbarMessage('No se detectaron signos de viruela de mono basados en los síntomas ingresados.');
          setSnackbarSeverity('success');
        }
        setOpenSnackbar(true);
      } else {
        console.error('Error:', response.statusText);
        setSnackbarMessage('Hubo un error al procesar tu solicitud. Por favor, inténtalo de nuevo.');
        setSnackbarSeverity('error');
        setOpenSnackbar(true);
      }
    } catch (error) {
      console.error('Error:', error);
      setSnackbarMessage('Hubo un error en la conexión. Por favor, revisa tu conexión a internet.');
      setSnackbarSeverity('error');
      setOpenSnackbar(true);
    }
  };

  const handleCloseSnackbar = () => {
    setOpenSnackbar(false);
  };

  return (
    <>
      <section id="predictionTool">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">

          <div className="py-12 md:py-20 border-t border-gray-800">

            {/* Section header */}
            <div className="max-w-3xl mx-auto text-center pb-12 md:pb-20">
              <h2 className="h2 mb-4">Prediction Tool</h2>
              <p className="text-xl text-gray-400">Test Our Prediction Tool</p>
            </div>

            <form id="pred-tool" onSubmit={handleSubmit} style={{ color: 'black', fontFamily: "'Architects Daughter', sans-serif" }} className="w-full max-w-xl mx-auto  bg-white rounded shadow-md">

              <div className="text-center p-8">
                <h2 className="text-2xl font-bold">Mpox Symptom Self-Assessment Form</h2>
                <p className="text-sm mt-2 text-gray-600">
                  The following questions will assess your symptoms to evaluate the likelihood of monkeypox infection
                </p>
              </div>
              <hr className="border-t-1 border-gray-200" />

              <div className="flex flex-col space-y-4 p-6">
                <Stack
                  direction="column"
                  divider={<Divider orientation="horizontal" flexItem />}
                  spacing={2}
                >

                  <div className="flex flex-row justify-center align-center w-full max-w-lg">
                    <label className="text-lg font-medium pt-5">Do you have any of the following symptoms?</label>
                    <div className="flex flex-wrap justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="systemicIllness" value="lymphaden" className="mr-2" onChange={handleChange} />
                        lymphaden
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="systemicIllness" value="Fever" className="mr-2" onChange={handleChange} />
                        Fever
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="systemicIllness" value="myalgia" className="mr-2" onChange={handleChange} />
                        myalgia
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="systemicIllness" value="None" className="mr-2" onChange={handleChange} />
                        None
                      </label>
                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium pt-5">Do you suffer from rectal pain?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="rectalPain" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="rectalPain" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>


                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Is your throat feeling sore?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="soreThroat" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="soreThroat" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Are you experiencing penile edema?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="penileOedema" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="penileOedema" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Do you have any oral lesions?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="oralLesions" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="oralLesions" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Do you have a solitary lesion?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="solitaryLesion" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="solitaryLesion" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Are your tonsils swollen or enlarged?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="swollenTonsils" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="swollenTonsils" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Have you tested positive for an HIV infection?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="hivInfection" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input  required type="radio" name="hivInfection" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="flex flex-row justify-around align-center w-full max-w-lg">
                    <label className="text-lg font-medium">Have you been diagnosed with a sexually transmitted infection (STI)?</label>
                    <div className="flex justify-center space-x-4">
                      <label className="flex items-center">
                        <input required type="radio" name="sti" value="yes" className="mr-2" onChange={handleChange} />
                        Yes
                      </label>
                      <label className="flex items-center">
                        <input required type="radio" name="sti" value="no" className="mr-2" onChange={handleChange} />
                        No
                      </label>

                    </div>
                  </div>

                  <div className="text-center p-8">

                    <p className="text-sm mt-2 font-bold">
                      The results predicted by this model are not 100% accurate. For a more robust diagnosis please visit the doctor.
                    </p>
                  </div>
                </Stack>

                <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded w-full mt-4">
                  Submit
                </button>
              </div>
            </form>

          </div>
        </div>
      </section>


      <Snackbar
        open={openSnackbar}
        autoHideDuration={6000}
        onClose={handleCloseSnackbar}
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }} // Center horizontally and place at the bottom
        sx={{
          position: 'fixed',
          // bottom: '20px', 
          left: '50%',
          transform: 'translateX(-50%)',
          width: '80%', // Adjust width as needed
        }} >
        <Alert onClose={handleCloseSnackbar} severity={snackbarSeverity} sx={{ width: '100%', fontSize: '1.25rem', padding: '1rem' }}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </>
  );
};

export default PredictionTool;



