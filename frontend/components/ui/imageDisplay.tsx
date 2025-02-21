// components/ui/imageDisplay.tsx
import React from 'react'

type ImageDisplayProps = {
  imageUrl: string
  peopleCount: number
}

const ImageDisplay: React.FC<ImageDisplayProps> = ({ imageUrl, peopleCount }) => {
  return (
    <div style={{ textAlign: 'center' }}>
      <h3>People Detected: {peopleCount}</h3>
      <img src={imageUrl} alt="Visualized Detection" style={{ maxWidth: '100%' }} />
    </div>
  )
}

export default ImageDisplay
