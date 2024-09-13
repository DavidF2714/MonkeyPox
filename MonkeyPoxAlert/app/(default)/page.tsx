export const metadata = {
  title: 'MonkeyPoxAlert',
  description: 'mpox predictor',
}

import MainHeader from '@/components/MainHeader'
import About from '@/components/About'
import PredictionTool from '@/components/PredictionTool'
import Symptoms from '@/components/Symptoms'
import Overview from '@/components/Overview'

export default function Home() {
  return (
    <>
      <MainHeader />
      <About />
      <Overview />
      <Symptoms />
      <PredictionTool />
    </>
  )
}
